from django.urls import path
from app2 import views
app_name="app2"
urlpatterns = [
    path("index2",views.index,name="index2"),
    path("samp2/",views.samp2,name="samp2"),
]