from django.contrib import admin
from accounts.models import CustomUser,Student
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Student)