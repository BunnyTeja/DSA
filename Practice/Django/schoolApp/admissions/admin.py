from django.contrib import admin
from admissions.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'name','fathername', 'classname', 'contact']
# Register your models here.

# I am regestering student model along with studentadmin class
# to display the list of attributes that i define in the class
admin.site.register(Student,StudentAdmin)
