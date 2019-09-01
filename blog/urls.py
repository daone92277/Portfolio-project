from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name = "blog"),
    path("<int:blog_id>/",views.detail, name="detail")
   
]