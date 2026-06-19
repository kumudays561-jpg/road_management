from django.urls import path
from . import views

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('add/', views.add_complaint, name='add_complaint'),
    path(
    'engineer-dashboard/',
    views.engineer_dashboard,
    name='engineer_dashboard'
    ),
    path(
    'resolve/<int:complaint_id>/',
    views.update_status,
    name='resolve_complaint'
    ),


]