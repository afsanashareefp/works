from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from rest_framework.reverse import reverse
from django import forms


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='department', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse('college:course_by_department', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course', blank=True)
    seats = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def get_url(self):
        return reverse('college:CourDepdetail', args=[self.department.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Details(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20, null=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
    course =  models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)
    purpose = models.CharField(max_length=100, choices=[('purpose1', 'Purpose 1'), ('purpose2', 'Purpose 2')])
    materials_provided = models.BooleanField(default=False)

    def __str__(self):
        return self.name