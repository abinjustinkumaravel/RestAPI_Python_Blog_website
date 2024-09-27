from django.urls import path
from . import views



urlpatterns=[
    path("",views.index, name="index"),
    path("detail/<int:user_id>",views.detail, name="detail"),
    path("new_url",views.new_url, name="new_url"),
    path("old_url",views.old_url, name="old_url"),


]