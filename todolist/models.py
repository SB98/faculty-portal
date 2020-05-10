from django.db import models
from details.models import Faculty
# Create your models here.
from django.utils import timezone


class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name #name to be shown when called


class TodoList(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE) # a foreignkey
    # def_faculty=Faculty.get.filter(faculty_id="20CE001")
    def_faculty = str(Faculty.objects.get(faculty_id="20CE001"))
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE,default=def_faculty)

    class Meta:
        ordering = ["-created"] #ordering by the created field

    # def __str__(self):
    #     return self.title #name to be shown when called
