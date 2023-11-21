from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import Student, Teacher
from admissions.forms import studentModelForm
from admissions.forms import VendorForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

#function based views

def homepage(req):
    return render(req,'index.html')

def addAdmissions(req):
    form = studentModelForm
    studentForm = {'form':form}

    # this part will be executed after submitting the form
    if req.method == 'POST':
        form = studentModelForm(req.POST)
        if form.is_valid():
            form.save()
        return homepage(req)

    return render(req,'admissions/add-admissions.html', studentForm)

def addVendor(req):
    form = VendorForm
    vform ={'form':form}

    # this part will be executed after submitting the form
    if req.method == 'POST':
        form = VendorForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['item'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contact'])
        return homepage(req)

    return render(req,'admissions/add-vendor.html', vform)

def deleteStudent(req,id):
    student = Student.objects.get(id=id)
    student.delete()
    return admissionsReport(req)

def updateStudent(req,id):
    student = Student.objects.get(id=id)
    form = studentModelForm(instance = student)
    dict = {'form':form}
    if req.method == 'POST':
        form = studentModelForm(req.POST, instance=student)
        # we are specifing instance to make clear that we are not inserting a new
        # record we are just updating the current record
        if form.is_valid:
            form.save()
        return admissionsReport(req)
        # return ('/admissions/admreport') we can also redirect to the page using url
    return render(req,'admissions/update-admission.html',dict)


def admissionsReport(req):
    #get all students records as objects
    result = Student.objects.all()
    #store the student objects in dict
    students = {'allstudents':result}
    return render(req,'admissions/admissions-report.html',students)

#class based view
class FirstclassBasesView(View):
    def get(self,req):
        return HttpResponse("This is 1st cbv")

class TeacherRead(ListView):
    model = Teacher

class GetTeacher(DetailView):
    model = Teacher

class AddTeacher(CreateView):
    model = Teacher
    fields = ('name', 'exp', 'subject', 'contact')

class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ('name','contact') 

class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('listteachers')

