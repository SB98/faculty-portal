from django.urls import reverse, resolve


class TestUrls:

    def test_home_urls(self):
        path = reverse('home')
        assert resolve(path).view_name == 'home'

    def test_facultydetails_url(self):
        path = reverse('facultydetails', kwargs={'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'facultydetails'

    def test_create_qualification_url(self):
        path = reverse('create_qualification', kwargs={'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'create_qualification'

    def test_update_qualification_url(self):
        path = reverse('update_qualification', kwargs={'pk': 1, 'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'update_qualification'

    def test_delete_qualification_url(self):
        path = reverse('delete_qualification', kwargs={'pk': 1})
        assert resolve(path).view_name == 'delete_qualification'

    def test_create_organization_url(self):
        path = reverse('create_organization', kwargs={'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'create_organization'

    def test_update_organization_url(self):
        path = reverse('update_organization', kwargs={'pk': 1, 'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'update_organization'

    def test_delete_organization_url(self):
        path = reverse('delete_organization', kwargs={'pk': 1})
        assert resolve(path).view_name == 'delete_organization'

    def test_changeImage_url(self):
        path = reverse('changeImage')
        assert resolve(path).view_name == 'changeImage'

    def test_deleteImage(self):
        path = reverse('deleteImage')
        assert resolve(path).view_name == 'deleteImage'

    def test_create_certification_url(self):
        path = reverse('create_certification', kwargs={'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'create_certification'

    def test_update_certification_url(self):
        path = reverse('update_certification', kwargs={'pk': 1, 'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'update_certification'

    def test_delete_certification_url(self):
        path = reverse('delete_certification', kwargs={'pk': 1})
        assert resolve(path).view_name == 'delete_certification'

    def test_create_award_url(self):
        path = reverse('create_award', kwargs={'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'create_award'

    def test_update_award_url(self):
        path = reverse('update_award', kwargs={'pk': 1, 'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'update_award'

    def test_delete_award_url(self):
        path = reverse('delete_award', kwargs={'pk': 1})
        assert resolve(path).view_name == 'delete_award'

    def test_create_publication_url(self):
        path = reverse('create_publication', kwargs={'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'create_publication'

    def test_update_publication_url(self):
        path = reverse('update_publication', kwargs={'pk': 1, 'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'update_publication'

    def test_delete_publication_url(self):
        path = reverse('delete_publication', kwargs={'pk': 1})
        assert resolve(path).view_name == 'delete_publication'

    def test_update_teachinginterest_url(self):
        path = reverse('update_teachinginterest', kwargs={'pk': 1, 'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'update_teachinginterest'

    def test_update_specialization_url(self):
        path = reverse('update_specialization', kwargs={'pk': 1, 'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'update_specialization'

    def test_update_about_url(self):
        path = reverse('update_about', kwargs={'pk': 1, 'faculty_id': '20CE001'})
        assert resolve(path).view_name == 'update_about'


