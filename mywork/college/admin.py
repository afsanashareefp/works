from django.contrib import admin

# Register your models here.
from django.contrib import admin

from django.contrib import admin

# Register your models here.
from .models import Department, Course


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Department, DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'fee', 'seats', 'available', 'created', 'updated']
    list_editable = ['fee', 'seats', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Course, CourseAdmin)
