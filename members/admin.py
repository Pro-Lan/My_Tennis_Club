from django.contrib import admin
from django.db import models
from .models import Member
from .models import Court
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "age",)
class CourseAdmin(admin.ModelAdmin):
  list_display = ("name", "Type", "city",)
  
admin.site.register(Member, MemberAdmin)
admin.site.register(Court, CourseAdmin)