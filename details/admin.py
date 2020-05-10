from django.contrib import admin
from .models import Faculty, Qualification, Certification, Award, Publication, Organization

import datetime
# Register your models here.


class FacultyAdmin(admin.ModelAdmin):
    fields = ('faculty_name', 'phone', 'department', 'email', 'designation')
    list_display = ('faculty_id', 'faculty_name', 'phone', 'department',)
    list_filter = ('department', )

    def save_model(self, request, obj, form, change):
        year = datetime.datetime.now().year
        id1 = str(Faculty.objects.filter(department=obj.department).count()+1).zfill(3)
        print(id1)
        faculty_id = str(abs(year)%100) + str(obj.department) + id1
        print(faculty_id)
        obj.faculty_id = faculty_id
        # print(obj.faculty_id)
        super().save_model(request, obj, form, change)


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Qualification)
admin.site.register(Publication)
admin.site.register(Award)
admin.site.register(Organization)
admin.site.register(Certification)
admin.site.site_header = 'Faculty Portal Admin'
