from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home, name = 'home'),
    path('addemp/',views.register, name = 'addemp'),
    path('createleave/',views.createleave, name = 'createleave'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('allemp/', views.all_emp, name='allemp'),
    path('penddinglist/', views.pendinglist, name='penddinglist'),
    path('acceptedlist/', views.Acceptedlist, name='acceptedlist'),
    path('canceledlist/', views.canceledlist, name='canceledlist'),
    path('updateemp/<task_id>/', views.Update_emp, name='updateemp'),
    path('deleteemp/<task_id>/', views.delete_emp, name='daleteemp'),
    path('Yearleave/', views.Total_RemainingLeaves, name='Yearleave'),


   

]