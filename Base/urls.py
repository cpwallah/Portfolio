from django.urls import path 
from . import views

urlpatterns=[
    path('',views.Contact),
    # path('contact/',views.contact,name="savecontact")
]