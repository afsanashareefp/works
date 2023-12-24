from django.urls import path
from . import views

app_name = 'college'

urlpatterns = [
    path('', views.allCourDep, name='allCourDep'),
    path('<slug:c_slug>/', views.allCourDep, name='course_by_department'),
    path('<slug:c_slug>/,<slug:course_slug>/', views.courDep, name='CourDepdetail'),

    path('details_form/', views.details_form, name='details_form'),

]
