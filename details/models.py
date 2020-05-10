
from djongo import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
# from month.models import MonthField
import datetime
# from django_month_year_widget.widgets import MonthYearWidget


YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))

DEPT_LIST = [('CE', 'CE'), ('IT', 'IT'), ('IC', 'IC'), ('CL', 'CL'), ('EC', 'EC'), ('CH', 'CH'), ('MH', 'MH')]


class Topic(models.Model):
    topic_name = models.CharField(max_length=50, null=True)

    class Meta:
        abstract = True


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = (
            'topic_name',
        )


class Faculty(models.Model):
    faculty_id = models.CharField(max_length=7, null=False)
    faculty_name = models.CharField(max_length=30, null=True)
    designation = models.CharField(max_length=30, null=True)
    department = models.CharField(max_length=2, choices=DEPT_LIST, null=False, default='CE')
    image = models.FileField(upload_to='', blank=True, default='NoImage.png')
    # qualifications = models.ArrayField(model_container=Qualification, null=True)
    phone = PhoneNumberField(blank=False, null=False,)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(max_length=200, null=True)
    office = models.CharField(max_length=30, null=True)
    biography = models.TextField(null=True)
    specializations = models.ArrayField(model_container=Topic, model_form_class=TopicForm, null=True)
    teaching_interests = models.ArrayField(model_container=Topic, null=True)
    faculty_type = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name_plural = "faculties"


class Certification(models.Model):
    credential_title = models.CharField(max_length=30)
    credential_id = models.CharField(max_length=100)
    credential_url = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    issuing_organization = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)


class Qualification(models.Model):
    degree = models.CharField(max_length=30)
    institute = models.CharField(max_length=100)
    from_year = models.IntegerField('from year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    to_year = models.IntegerField('to year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    field = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Publication(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    publisher = models.CharField(max_length=30)
    publication_date = models.DateField()
    publication_url = models.URLField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Award(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    issuer = models.CharField(max_length=30)
    issue_date = models.DateField()
    association = models.CharField(max_length=30)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Organization(models.Model):
    organization_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    description = models.TextField()
    employment_type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    from_year = models.IntegerField('from year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    to_year = models.IntegerField('to year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    is_currently_working = models.BooleanField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)





