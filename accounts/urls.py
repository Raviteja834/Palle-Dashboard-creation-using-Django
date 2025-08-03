from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('employee_list/',views.employee_list,name='employee_list'),
    path('student_list/',views.student_list,name='student_list'),
    path('addnew/',views.new_student,name='new_student'),
    path('update/<int:id>',views.update_student,name='update'),
    path('delete/<int:id>',views.delete_student,name='delete'),
]