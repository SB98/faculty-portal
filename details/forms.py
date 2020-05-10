# Normal Imports

from .models import Faculty
from .models import Organization, Certification
from .models import Qualification
from .models import Award,Publication
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from .models import *


# Normal Code begins

class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['image']


class QualificationForm(BSModalForm):

    class Meta:
        model = Qualification
        fields = '__all__'

    def __init__(self, faculty_id=None, pk=None , *args, **kwargs):
        super(QualificationForm, self).__init__(*args, **kwargs)
        l = str(kwargs['request']).split('/')
        faculty_id = l[-2]
        faculty = Faculty.objects.get(faculty_id=faculty_id)
        print(self.fields)
        self.fields['faculty'].initial = faculty
        self.fields['faculty'].widget = forms.HiddenInput()
        self.fields['faculty'].label = ''
        print(faculty_id, 'Form')  # prints the value of the foo url conf param


class AboutForm(BSModalForm):

    class Meta:
        model = Faculty
        fields = ['biography']


class OrganizationForm(BSModalForm):

    class Meta:
        model = Organization
        fields = '__all__'
        # widgets = {
        #     'from_date': DateInput(),
        #     'to_date': DateInput(),
        # }

    def __init__(self, faculty_id=None, pk=None, *args, **kwargs):
        super(OrganizationForm, self).__init__(*args, **kwargs)
        l = str(kwargs['request']).split('/')
        faculty_id = l[-2]
        faculty = Faculty.objects.get(faculty_id=faculty_id)
        print(self.fields)
        self.fields['faculty'].initial = faculty
        self.fields['faculty'].widget = forms.HiddenInput()
        self.fields['faculty'].label = ''
        print(faculty_id, 'Form')  # prints the value of the foo url conf param


class CertificationForm(BSModalForm):

    class Meta:
        model = Certification
        fields = '__all__'

    def __init__(self, faculty_id=None, pk=None, *args, **kwargs):
        super(CertificationForm, self).__init__(*args, **kwargs)
        l = str(kwargs['request']).split('/')
        faculty_id = l[-2]
        faculty = Faculty.objects.get(faculty_id=faculty_id)
        print(self.fields)
        self.fields['faculty'].initial = faculty
        self.fields['faculty'].widget = forms.HiddenInput()
        self.fields['faculty'].label = ''
        print(faculty_id, 'Form')  # prints the value of the foo url conf param


class SpecializationForm(BSModalForm):

    class Meta:
        model = Faculty
        fields = ['specializations']


class PublicationForm(BSModalForm):

    class Meta:
        model = Publication
        fields = '__all__'
        widgets = {
            'publication_date': DateInput(),
        }

    def __init__(self, faculty_id=None, pk=None, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)
        l = str(kwargs['request']).split('/')
        faculty_id = l[-2]
        faculty = Faculty.objects.get(faculty_id=faculty_id)
        print(self.fields)
        self.fields['faculty'].initial = faculty
        self.fields['faculty'].widget = forms.HiddenInput()
        self.fields['faculty'].label = ''
        print(faculty_id, 'Form')  # prints the value of the foo url conf param


class AwardForm(BSModalForm):

    class Meta:
        model = Award
        fields = '__all__'
        widgets = {
            'issue_date': DateInput(),
        }

    def __init__(self, faculty_id=None, pk=None, *args, **kwargs):
        super(AwardForm, self).__init__(*args, **kwargs)
        l = str(kwargs['request']).split('/')
        faculty_id = l[-2]
        faculty = Faculty.objects.get(faculty_id=faculty_id)
        print(self.fields)
        self.fields['faculty'].initial = faculty
        self.fields['faculty'].widget = forms.HiddenInput()
        self.fields['faculty'].label = ''
        print(faculty_id, 'Form')  # prints the value of the foo url conf param


class TeachingInterestForm(BSModalForm):

    class Meta:
        model = Faculty
        fields = ['teaching_interests']


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
