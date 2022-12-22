from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import SessionYear,AdminHOD, Professor, Courses, Subjects, Students,Exam


admin.site.register(SessionYear)
# class SessionYearModel(admin.ModelAdmin):
#     list_display = [field.name for field in SessionYear._meta.get_fields()]
admin.site.register(AdminHOD)
admin.site.register(Professor)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Exam)

