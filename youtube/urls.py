from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='youtube_home'),
    path('search/<str:query>', views.search),
    path('videos/<str:title>/', views.videos, name='youtube_videos'),
    path('videos/<str:title>/<int:id>/<str:video>', views.video, name='youtube_video'),
]