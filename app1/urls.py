from django.urls import path
from app1 import views
app_name="app1"
urlpatterns = [
    path("",views.index,name="index1"),
    path("samp1/",views.samp1,name="samp1"),
]