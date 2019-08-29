from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('create/', views.create, name="create"),
    path('(?P<pk>[0-9]+)/upvote', views.upvote, name="upvote"),
    path('(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    path('user/(?P<fk>[0-9]+)', views.userposts, name='userposts'),
 ]