from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<subject>/<number>/', views.course_sections, name='course_sections'),
    path('<subject>/<number>/<sectionName>', views.subscribe, name='subscribe'),
]
