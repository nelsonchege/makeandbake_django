from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.said_hello),
    path('blogs_paths/',views.blogs_paths),
    path('blog_list/',views.bloglist),
    path('createblog/',views.createblog),
    path('updateblog/<str:pk>/',views.updateblog),
    path('deleteblog/<str:pk>/',views.deleteblog),
    path('oneblog/<str:pk>/',views.oneblog),
]