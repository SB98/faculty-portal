from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import datetime
from details.models import *
import time
from twilio.rest import Client
from . import api


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def auth_view(request):
    try:
        username = request.POST.get('username', '').upper()
        password = request.POST.get('password', '')
        if request.user.is_authenticated:
            '''if request.user.is_superuser:
                return render(request,' index.html')'''
            return HttpResponseRedirect('/polls/facultydetails/'+username.upper()+'/')

        user = auth.authenticate(username=username.upper(), password=password)
        if user is not None:
            auth.login(request, user)
            print("logged in")
            request.session['faculty_id'] = username
            return HttpResponseRedirect('/polls/facultydetails/'+username+'/#')

        else:
            print("incorrect cred")
            messages.add_message(request, messages.WARNING,
                                 'Incorrect Username or Password')
            return HttpResponseRedirect('/login/login')
    except:
        return render(request, 'login.html')


@login_required()
def logout(request):
    try:
        if request.user.is_authenticated:
            auth.logout(request)
        messages.add_message(request, messages.INFO,
                             'You are Successfully Logged Out')
        messages.add_message(request, messages.INFO, 'Thanks for visiting.')
        # request.session.clear()
        return HttpResponseRedirect('/login/')
    except:
        messages.add_message(request, messages.WARNING,
                             'exception Occured..please try again.')
        return render(request, ' login.html')


def createPassword(request, faculty_id='16CE001'):
    print("create")
    return render(request, 'password.html', {'faculty_id': faculty_id})


def changeUser(request):
    username = request.POST.get('faculty_id', '')
    password = request.POST.get('password', '')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None
    if user:
        user.set_password(password)
        user.save()
    else:
        u = User.objects.create_user(username=username.upper(), password=password)
        u.save()

    return HttpResponseRedirect("/login/")


def change(request):
    # c = {}
    # c.update(csrf(request))
    return render(request, 'change.html', {'sent': False})


def generatePassword(request):
    client = Client(api.account_sid, api.auth_token)
    faculty_id = request.POST.get('faculty_id').upper()
    if(faculty_id == None):
        return HttpResponseRedirect('/login/change')
    # faculty_id = '16CE001'
    faculty = Faculty.objects.filter(faculty_id=faculty_id).first()
    # print('faculty',faculty)
    phone = faculty.phone.__str__()
    verification = client.verify.services(
        api.service_sid).verifications.create(to=phone, channel='sms')
    print(verification.status)
    return render(request, 'change.html', {'sent': True, 'phone': phone, 'faculty_id': faculty_id})


def verify(request):
    otp = request.POST.get('otp')
    phone = request.POST.get('phone')
    faculty_id = request.POST.get('faculty_id').upper()
    if(phone == None):
        return HttpResponseRedirect('/login/change')
    client = Client(api.account_sid, api.auth_token)
    verification_check = client.verify \
        .services(api.service_sid) \
        .verification_checks \
        .create(to=phone, code=otp)

    # print(verification_check.status)
    if(verification_check.status == 'approved'):
        url = '/login/createPassword/'+faculty_id
        return HttpResponseRedirect(url)
    return render(request, 'change.html', {'sent': True, 'phone': phone, 'faculty_id': faculty_id, 'message': 'otp not verified!! reenter'})
