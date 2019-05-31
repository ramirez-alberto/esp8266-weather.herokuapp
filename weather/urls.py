from django.urls import path

from . import views

app_name = 'weather'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('form/',views.form,name = 'form_submit'),
    path('landing/',views.form,name = 'landing'),
]