from django.urls import path


from django.conf.urls import url
from . import views

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# login, auth_view,


urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'^facultydetails/(?P<faculty_id>[a-zA-Z0-9]+)/$', views.facultydetails, name='facultydetails'),

    url(r'^create_qualification/(?P<faculty_id>[a-zA-Z0-9]+)/$', views.QualificationCreateView.as_view(),
        name='create_qualification'),
    url(r'^create_organization/(?P<faculty_id>[a-zA-Z0-9]+)/$', views.OrganizationCreateView.as_view(),
        name='create_organization'),
    url(r'^create_certification/(?P<faculty_id>[a-zA-Z0-9]+)/$', views.CertificationCreateView.as_view(),
        name='create_certification'),
    url(r'^create_award/(?P<faculty_id>[a-zA-Z0-9]+)/$', views.AwardCreateView.as_view(), name='create_award'),
    url(r'^create_publication/(?P<faculty_id>[a-zA-Z0-9]+)/$', views.PublicationCreateView.as_view(),
        name='create_publication'),

    url(r'^update_qualification/(?P<faculty_id>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', views.QualificationUpdateView.as_view(),
        name='update_qualification'),
    url(r'^update_about/(?P<faculty_id>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', views.AboutUpdateView.as_view(),
        name='update_about'),
    url(r'^update_organization/(?P<faculty_id>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', views.OrganizationUpdateView.as_view(),
        name='update_organization'),
    url(r'^update_certification/(?P<faculty_id>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', views.CertificationUpdateView.as_view(),
        name='update_certification'),
    url(r'^update_publication/(?P<faculty_id>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', views.PublicationUpdateView.as_view(),
        name='update_publication'),
    url(r'^update_award/(?P<faculty_id>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', views.AwardUpdateView.as_view(),
        name='update_award'),
    url(r'^update_teachinginterest/(?P<faculty_id>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$',
        views.TeachingInterestUpdateView.as_view(), name='update_teachinginterest'),
    url(r'^update_specialization/(?P<faculty_id>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$',
        views.SpecializationUpdateView.as_view(), name='update_specialization'),

    path('delete_qualification/<int:pk>', views.QualificationDeleteView.as_view(), name='delete_qualification'),
    path('delete_organization/<int:pk>', views.OrganizationDeleteView.as_view(), name='delete_organization'),
    path('delete_certification/<int:pk>', views.CertificationDeleteView.as_view(), name='delete_certification'),
    path('delete_award/<int:pk>', views.AwardDeleteView.as_view(), name='delete_award'),
    path('delete_publication/<int:pk>', views.PublicationDeleteView.as_view(), name='delete_publication'),

    path('success', success, name='success'),
    path('changeImage', changeImage, name='changeImage'),
    path('deleteImage', deleteImage, name='deleteImage'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
