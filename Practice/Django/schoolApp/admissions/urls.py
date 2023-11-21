from django.urls import path
from admissions.views import addAdmissions
from admissions.views import admissionsReport
from admissions.views import addVendor
from admissions.views import deleteStudent
from admissions.views import updateStudent
from admissions.views import FirstclassBasesView
from admissions.views import TeacherRead
from admissions.views import GetTeacher
from admissions.views import AddTeacher
from admissions.views import UpdateTeacher
from admissions.views import DeleteTeacher

urlpatterns = [
  
    path('newadm/', addAdmissions),
    path('admreport/', admissionsReport),
    path('newvendor/', addVendor),
    path('delete/<int:id>', deleteStudent),
    path('update/<int:id>', updateStudent),
    path('firstcbv/', FirstclassBasesView.as_view()),
    path('teacherslist/', TeacherRead.as_view(), name = 'listteachers'),
    path('getteacherdetail/<int:pk>', GetTeacher.as_view()),
    path('insertteacher/', AddTeacher.as_view()),
    path('updateteacher/<int:pk>', UpdateTeacher.as_view()),
    path('deleteteacher/<int:pk>', DeleteTeacher.as_view()),
]