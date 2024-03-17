from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/EventApp/booking/',views.admin_update,name='admin_update'),
    path('admin/',views.admin,name='admin'),
    path('saved/',views.saved,name='saved'),
    path('about/',views.about,name='about'),
    path('events/',views.events,name='events'),
    path('contact/',views.contact,name='contact'),
    path('booking/',views.booking,name='booking'),
]
