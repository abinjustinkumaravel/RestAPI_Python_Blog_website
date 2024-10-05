from django.urls import path
from . import views

app_name= "blog"

urlpatterns=[
    path("",views.index, name="index"),
    path("post/<int:post_id>", views.detail, name="detail"),
    path("new_test_url",views.new_url, name="new_url"),
    path("old_url",views.old_url, name="old_url"),
]