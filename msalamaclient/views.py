import  datetime
from django.http import JsonResponse
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import ListView, FormView, View
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from forms import SignupForm, UserProfileForm, VaccineReportForm, VaccineReceivedReportForm, MakeAppointmentForm, MessageSentForm
from models import UserProfile, PatientVaccination, VaccineDose, Vaccine, Appointment, Message


class GraphDataView(View):
    def get(self, request, *args, **kwargs):

        data_type = request.GET.get('type')
        if data_type == 'patients_graph':
            groups = PatientVaccination().monthly_patients()

            availaible_months = groups.keys()
            data = []

            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            for month in months:
                if month in availaible_months:
                    data.append(groups[month])
                else:
                    data.append(0)

            data = [{
                'name': 'Recipient',
                'data': ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
            }, {
                'name': 'Number of Patients',
                'data': data
            }]

        elif data_type == 'vaccine_graph':
            groups = PatientVaccination().monthly_vaccine()

            data = []

            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

            vaccine_dict = {}
            for vaccine in Vaccine.objects.all():
                vaccine_dict[vaccine.vaccinename] = []

            for month in months:
                for vaccine in vaccine_dict:
                    if not groups[(groups.month == month) & (groups.patient_vaccine == vaccine)]['count'].empty:
                        vaccine_dict[vaccine].append(int(groups[(groups.month == month) & (groups.patient_vaccine == vaccine)]['count']))
                    else:
                        vaccine_dict[vaccine].append(0)

            for key, value in vaccine_dict.iteritems():
                data.append({'name': key, 'data': value})

        else:
            data = []

        return JsonResponse(data, safe=False)


# Create your views here.
def login(request):
    #assert False, request
    c={}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        try:
            p = UserProfile.objects.get(user__username=request.POST['username'])
        except UserProfile.DoesNotExist:
            return HttpResponseRedirect('userprofile')
        
        if p.IDNum is not None:
            request.session['user_sysID']=p.IDNum
            return HttpResponseRedirect('loggedin.html')
        else:
            return HttpResponseRedirect('userprofile')
    
        
    else:
        return HttpResponseRedirect('invalid_login.html')

def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.session['user_sysID']})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('signup_success')
        
    args={}
    args.update(csrf(request))
    args['form'] = SignupForm()
    return render_to_response('signup.html', args)


def signup_success(request):
    return render_to_response('signup_success.html')

def vaccines(request):
    return render_to_response('vaccines.html')


def childvaccines(request):
    return render_to_response('childvaccines.html')


def polio(request):


    #Get count of doses 
    vaccdosescount = VaccineDose.objects.filter(vaccine__vaccinename='Polio Sabin Vaccine').count()
    #GET NO OF DOSES RECIEVED
    count =PatientVaccination.objects.filter(patient__IDNum=request.session['user_sysID']).filter(patient_vaccine__vaccinename='Polio Sabin Vaccine').count()
    #PERCENTAGE DOSES RECIEVED
    percentagevaccinated=0

    if count:
        if vaccdosescount:
            percentagevaccinated= int(count/float(vaccdosescount)*100)


    #ALL DOSES REQUIRED
    poliovaccinedoses  =VaccineDose.objects.filter(vaccine__vaccinename='Polio Sabin Vaccine').order_by("vaccinedose")
    #DOSES RECIEVED SO FAR
    poliovaccinedosesrecieved =PatientVaccination.objects.filter(patient__IDNum=request.session['user_sysID']).filter(patient_vaccine__vaccinename='Polio Sabin Vaccine')
    poliovaccinedosesrecieved_ids = [vaccine.vaccinedose.id for vaccine in poliovaccinedosesrecieved]


    lsrecieved=[]
    lspending=[]
    lista= []



    pending = [vaccine for vaccine in poliovaccinedoses if vaccine.id not in poliovaccinedosesrecieved_ids]
    received = [vaccine for vaccine in poliovaccinedoses if vaccine.id in poliovaccinedosesrecieved_ids]


    return render_to_response('polio.html', {'percentagedose': percentagevaccinated, 'vaccinesrecieved': received, 'vaccinesrequired': pending})


    

@login_required
def userprofile(request):
    if request.method=="POST":
        form=UserProfileForm(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect('signup_success')
    else:
        args ={}
        args.update(csrf(request))
        args['form']=UserProfileForm()
    return render_to_response('userprofile.html', args)


class VaccineReceivedReportView(FormView):
    form_class = VaccineReceivedReportForm
    template_name = 'vaccinereceived.html'

    def form_valid(self, form):
        form.instance.vaccinedose = VaccineDose.objects.get(id=self.request.GET.get('dose'))
        form.instance.patient_vaccine = Vaccine.objects.get(id=self.request.GET.get('vaccine'))
        form.instance.patient = self.request.user.userprofile
        form.save()
        messages.success(self.request, 'Vaccine updated successfully. Thank you.')
        return HttpResponseRedirect(reverse('vaccinereceived'))



class MakeAppointmentFormView(FormView):
    form_class = MakeAppointmentForm
    template_name='appointment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render_to_response(self.template_name, {'form':form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        form.instance.firstchoicedate = form.cleaned_data.get('firstchoicedate')
        form.instance.secondchoicedate = form.cleaned_data.get('secondchoicedate')
        form.instance.purposeofvisit = form.cleaned_data.get('purposeofvisit')
        form.instance.patient = self.request.user.userprofile
        form.save()
        messages.success(self.request, 'Appointment added successfully. Thank you!')
        return HttpResponseRedirect(reverse('makeappointment'))


class SendMessageFormView(FormView):
    form_class = MessageSentForm
    template_name = 'sendmessage.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render_to_response(self.template_name, {'form':form}, context_instance=RequestContext(request))

    def form_valid(self, form):
        form.instance.message=form.cleaned_data.get('message')
        form.instance.messagesubject=form.cleaned_data.get('messagesubject')
        form.instance.patient=self.request.user.userprofile
        form.save()
        messages.success(self.request, 'Message successfully sent. Thank you, we shall get back to you')
        return HttpResponseRedirect(reverse('sendmessage'))

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment_list.html'

    def get_queryset(self):
        queryset = super(AppointmentListView, self).get_queryset()
        queryset = queryset.filter(patient=self.request.user.userprofile)
        return queryset


def Messages(request):
     if request.method=="GET":
        model = Message
        template_name = 'messages.html'

        # queryset= super(MessagesListView, self).get_queryset()
        queryset = Message.objects.filter(patient=request.user.userprofile)
        queryset1 = queryset.distinct('date')
        return render_to_response('messages.html', {'datehead': queryset1, 'datedmessages': queryset })


def reportvaccine(request):

    if request.method=="POST":


        form = VaccineReportForm(request.POST)

        if form.is_valid():
            form.instance.patient= UserProfile.objects.get(IDNum=request.user.userprofile)

            form.instance.vaccine= Vaccine.objects.get(vaccineIDnum = request.POST.get('Vaccine'))

            form.save()

            messages.success(request, 'Report successfully sent. Thank you.')
            return HttpResponseRedirect(reverse('reportvaccine'))

    args={}
    args.update(csrf(request))
    args['form'] = VaccineReportForm()

    return render_to_response('vaccinereport.html', args)





