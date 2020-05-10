# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render
from django.template import RequestContext
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views import generic
from todolist.models import TodoList
from django.utils import timezone
from chat.models import Message
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import QualificationForm, CustomUserCreationForm, CustomAuthenticationForm, PublicationForm, AwardForm,\
    CertificationForm, OrganizationForm, TeachingInterestForm, SpecializationForm, AboutForm, ProfileForm
from .models import Faculty

from .models import *



#
# class FacultyDetails(generic.ListView):
#     model = Faculty
#     context_object_name = 'faculty'
#     template_name = 'facultydetails.html'

from django.shortcuts import redirect
from .forms import *


@login_required
def changeImage(request):
    faculty_id = request.POST.get('faculty_id', '')
    image = request.FILES['profile']
    print('image post', image)
    faculty = Faculty.objects.filter(faculty_id=faculty_id).first()
    faculty.image = image
    faculty.save()
    print("image after save",faculty.image)
    # handle_uploaded_file(faculty_id,image)
    # faculty = Faculty.objects.filter(
    #     faculty_name=faculty_id).update(image=image)
    return HttpResponseRedirect('/polls/facultydetails/'+faculty_id+'/')


@login_required
def deleteImage(request):
    faculty_id = request.POST.get('faculty_id', '')
    image = "NoImage.png"
    faculty = Faculty.objects.get(faculty_id=faculty_id)
    faculty.image = image
    faculty.save()
    return HttpResponseRedirect('/polls/facultydetails/'+faculty_id+'/')


def success(request):
    return HttpResponse('successfully uploaded')


def profile_image_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render_to_response('facultydetails.html', context_instance=RequestContext(request))
    else:
        form = ProfileForm()
    return render(request, 'profile_image_form.html', {'form': form})


class QualificationCreateView(BSModalCreateView):
    form_class = QualificationForm
    template_name = 'create_qualification.html'
    success_message = 'Success: Qualification was created.'

    def get_form_kwargs(self):
        kwargs = super(QualificationCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        print('request', self.request.session.get('faculty_id', None))
        return kwargs

    def get_success_url (self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class CertificationCreateView(BSModalCreateView):
    template_name = 'create_qualification.html'
    form_class = CertificationForm
    success_message = 'Success: Certification was created.'

    def get_form_kwargs(self):
        kwargs = super(CertificationCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class PublicationCreateView(BSModalCreateView):
    template_name = 'create_qualification.html'
    form_class = PublicationForm
    success_message = 'Success: Publication was created.'

    def get_form_kwargs(self):
        kwargs = super(PublicationCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AwardCreateView(BSModalCreateView):
    template_name = 'create_qualification.html'
    form_class = AwardForm
    success_message = 'Success: Award was created.'

    def get_form_kwargs(self):
        kwargs = super(AwardCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class OrganizationCreateView(BSModalCreateView):
    template_name = 'create_qualification.html'
    form_class = OrganizationForm
    success_message = 'Success: Organization was created.'

    def get_form_kwargs(self):
        kwargs = super(OrganizationCreateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


# update views
class QualificationUpdateView(BSModalUpdateView):
    model = Qualification
    template_name = 'update_qualification.html'
    form_class = QualificationForm
    success_message = 'Success: Qualification was updated.'

    def get_form_kwargs(self):
        kwargs = super(QualificationUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AboutUpdateView(BSModalUpdateView):
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = AboutForm
    success_message = 'Success: About was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class CertificationUpdateView(BSModalUpdateView):
    model = Certification
    template_name = 'update_qualification.html'
    form_class = CertificationForm
    success_message = 'Success: Certification was updated.'

    def get_form_kwargs(self):
        kwargs = super(CertificationUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AwardUpdateView(BSModalUpdateView):
    model = Award
    template_name = 'update_qualification.html'
    form_class = AwardForm
    success_message = 'Success: Certification was updated.'

    def get_form_kwargs(self):
        kwargs = super(AwardUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class PublicationUpdateView(BSModalUpdateView):
    model = ProfileForm
    template_name = 'update_qualification.html'
    form_class = PublicationForm
    success_message = 'Success: Certification was updated.'

    def get_form_kwargs(self):
        kwargs = super(PublicationUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class TeachingInterestUpdateView(BSModalUpdateView):
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = TeachingInterestForm
    success_message = 'Success: Teaching Interest was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class SpecializationUpdateView(BSModalUpdateView):
    model = Faculty
    template_name = 'update_qualification.html'
    form_class = SpecializationForm
    success_message = 'Success: Specialization was updated.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class OrganizationUpdateView(BSModalUpdateView):
    model = Organization
    template_name = 'update_qualification.html'
    form_class = OrganizationForm
    success_message = 'Success: Organization was updated.'

    def get_form_kwargs(self):
        kwargs = super(OrganizationUpdateView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)
        print(kwargs['request'])
        global faculty_id
        faculty_id = kwargs['faculty_id']
        # print(faculty_id)# self.kwargs contains all url conf params
        print(faculty_id, 'views')
        return kwargs

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class QualificationReadView(BSModalReadView):
    model = Faculty
    template_name = 'read_qualification.html'


# Delete Views
class QualificationDeleteView(BSModalDeleteView):
    model = Qualification
    template_name = 'delete_qualification.html'
    success_message = 'Success: Qualification was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class OrganizationDeleteView(BSModalDeleteView):
    model = Organization
    template_name = 'delete_qualification.html'
    success_message = 'Success: Organization was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class CertificationDeleteView(BSModalDeleteView):
    model = Certification
    template_name = 'delete_qualification.html'
    success_message = 'Success: Certification was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class AwardDeleteView(BSModalDeleteView):
    model = Award
    template_name = 'delete_qualification.html'
    success_message = 'Success: Award was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


class PublicationDeleteView(BSModalDeleteView):
    model = Publication
    template_name = 'delete_qualification.html'
    success_message = 'Success: Publication was deleted.'

    def get_success_url(self):
        return reverse_lazy('facultydetails', kwargs={'faculty_id': self.request.session.get('faculty_id', None)})


def facultydetails(request, faculty_id):
    print("faculty: ", faculty_id)

    faculty = Faculty.objects.get(faculty_id=faculty_id)
    qualification = Qualification.objects.all().filter(faculty=faculty)
    publication = Publication.objects.all().filter(faculty=faculty)
    award = Award.objects.all().filter(faculty=faculty)
    organization = Organization.objects.all().filter(faculty=faculty)
    certification = Certification.objects.all().filter(faculty=faculty)
    login_faculty_id = request.session.get('faculty_id', None)
    latest_messages = Message.objects.filter(sender=request.user.id)

    todos=[]
    if login_faculty_id==faculty.faculty_id:
        todos = TodoList.objects.filter(faculty=Faculty.objects.get(faculty_id=request.session.get('faculty_id', None)))  # quering all todos with the object mana
    notificationArr = []
    if (todos):
        for todo in todos:
            print(todo.due_date, timezone.now().strftime("%Y-%m-%d"))
            if str(todo.due_date) == str(timezone.now().strftime("%Y-%m-%d")):
                print(todo.due_date, timezone.now().strftime("%Y-%m-%d"))
                notificationArr.append(todo)
    todo_no = len(notificationArr)
    print("notificai", notificationArr)
    if qualification:
        latest_qualification = Qualification.objects.all().filter(faculty=faculty).latest('to_year')
    else:
        latest_qualification=None
    print('latest Q', latest_qualification)
    print(qualification, 'q')
    login_faculty_id = request.session.get('faculty_id', None)
    print('login_fid', login_faculty_id)

    if login_faculty_id==faculty.faculty_id:
        print("same login")

    print("ID's",login_faculty_id,faculty.faculty_id)
    faculties = Faculty.objects.filter()
    users = User.objects.exclude(username=request.user.username)
    latest_msgs = []
    print('users:', users)
    for user in users:
        print("id", user.id, user.username)
        latest_msg = Message.objects.filter(sender=user.id, receiver=request.user.id).order_by('-timestamp').first()
        # if latest_msg is not None:
        latest_msgs.append(latest_msg)

    print('lms', latest_msgs)
    context = {'faculty': faculty, 'qualifications': qualification, 'publications': publication, 'awards': award, 'organizations': organization, 'certifications': certification, 'latest_qualification': latest_qualification, 'login_faculty_id': login_faculty_id, 'todo_no': todo_no, 'notificationArr': notificationArr, 'faculties': faculties, 'users': users, 'sid': request.user.id, 'request': request, 'latest_msgs': latest_msgs}
    context.update(csrf(request))
    return render_to_response('facultydetails.html', context)


def home(request):
    # auth.logout(request)
    if request.method == "GET":
        query = request.GET.get('Search')
        print("search", query)
        if query:
            faculties = Faculty.objects.filter(Q(faculty_name__icontains=query) | Q(department__icontains=query) | Q(faculty_id__icontains=query))
            # for faculty in faculties:
            #     qualification = Qualification.objects.filter(faculty=faculty,degree=query)
            #     if qualification:
            #         pass

            # print(faculties)
        else:
            faculties = Faculty.objects.filter()
    login_faculty_id = request.session.get('faculty_id', None)
    return render_to_response('home.html', {"faculties": faculties, 'login_faculty_id': login_faculty_id,'request':request})
