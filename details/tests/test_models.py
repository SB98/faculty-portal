from django.test import TestCase
from details.models import Faculty, Qualification, Certification, Award, Publication, Organization
import datetime


class FacultyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Faculty.objects.create(faculty_id='20ME001', faculty_name='G. D . Bassan', designation='Head of Dept', department='ME', phone='+918160496426')

    def test_faculty_id_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('faculty_id').verbose_name
        self.assertEqual(field_label, 'faculty id')

    def test_faculty_name_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('faculty_name').verbose_name
        self.assertEqual(field_label, 'faculty name')

    def test_designation_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('designation').verbose_name
        self.assertEqual(field_label, 'designation')

    def test_department_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('department').verbose_name
        self.assertEqual(field_label, 'department')

    # def test_phone_label(self):
    #     obj = Faculty.objects.filter().order_by('-id')[0]
    #     id1 = obj.id
    #     faculty = Faculty.objects.get(id=id1)
    #     field_label = faculty._meta.get_field('phone').verbose_name
    #     self.assertEqual(field_label, 'phone')

    def test_email_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_office_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('office').verbose_name
        self.assertEqual(field_label, 'office')

    def test_website_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('website').verbose_name
        self.assertEqual(field_label, 'website')

    def test_biography_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('biography').verbose_name
        self.assertEqual(field_label, 'biography')

    def test_specializations_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('specializations').verbose_name
        self.assertEqual(field_label, 'specializations')

    def test_teaching_interests_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('teaching_interests').verbose_name
        self.assertEqual(field_label, 'teaching interests')

    def test_faculty_type_label(self):
        obj = Faculty.objects.filter().order_by('-id')[0]
        id1 = obj.id
        faculty = Faculty.objects.get(id=id1)
        field_label = faculty._meta.get_field('faculty_type').verbose_name
        self.assertEqual(field_label, 'faculty type')

# We chose to use assertEqual(field_label,'first name') rather
#  than assertTrue(field_label == 'first name').
#  The reason for this is that if the test fails the output
#  for the former tells you what the label actually was,
#  which makes debugging the problem just a little easier.


class QualificationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        faculty = Faculty.objects.create(faculty_id='20ME001', faculty_name='G. D . Bassan', designation='Head of Dept',
                               department='ME', phone='+918160496426')
        Qualification.objects.create(degree='M.TEch', institute='IIT', from_year=2016, to_year=2018, faculty=faculty)

    def test_degree_label(self):
        obj = Qualification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        qualification = Qualification.objects.get(id=id1)
        field_label = qualification._meta.get_field('degree').verbose_name
        self.assertEqual(field_label, 'degree')

    def test_institute_label(self):
        obj = Qualification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        qualification = Qualification.objects.get(id=id1)
        field_label = qualification._meta.get_field('institute').verbose_name
        self.assertEqual(field_label, 'institute')

    def test_from_year_label(self):
        obj = Qualification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        qualification = Qualification.objects.get(id=id1)
        field_label = qualification._meta.get_field('from_year').verbose_name
        self.assertEqual(field_label, 'from year')

    def test_to_year_label(self):
        obj = Qualification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        qualification = Qualification.objects.get(id=id1)
        field_label = qualification._meta.get_field('to_year').verbose_name
        self.assertEqual(field_label, 'to year')

    def test_faculty_label(self):
        obj = Qualification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        qualification = Qualification.objects.get(id=id1)
        field_label = qualification._meta.get_field('faculty').verbose_name
        self.assertEqual(field_label, 'faculty')


class CertificationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        faculty = Faculty.objects.create(faculty_id='20ME001', faculty_name='G. D . Bassan', designation='Head of Dept',
                                         department='ME', phone='+918160496426')
        Certification.objects.create(credential_title='ML using python', credential_id='123456', credential_url='www.coursera.com/123456/', issue_date=datetime.date.today(), expiration_date=datetime.date.today(), faculty=faculty, issuing_organization='IBM')

    def test_credential_title_label(self):
         obj = Certification.objects.filter().order_by('-id')[0]
         id1 = obj.id
         certification = Certification.objects.get(id=id1)
         field_label = certification._meta.get_field('credential_title').verbose_name
         self.assertEqual(field_label, 'credential title')

    def test_credential_id_label(self):
        obj = Certification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        certification = Certification.objects.get(id=id1)
        field_label = certification._meta.get_field('credential_id').verbose_name
        self.assertEqual(field_label, 'credential id')

    def test_credential_url_label(self):
        obj = Certification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        certification = Certification.objects.get(id=id1)
        field_label = certification._meta.get_field('credential_url').verbose_name
        self.assertEqual(field_label, 'credential url')

    def test_issuing_organization_label(self):
        obj = Certification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        certification = Certification.objects.get(id=id1)
        field_label = certification._meta.get_field('issuing_organization').verbose_name
        self.assertEqual(field_label, 'issuing organization')

    def test_faculty_label(self):
        obj = Certification.objects.filter().order_by('-id')[0]
        id1 = obj.id
        certification = Certification.objects.get(id=id1)
        field_label = certification._meta.get_field('faculty').verbose_name
        self.assertEqual(field_label, 'faculty')
