from django.urls import path
from . import views


app_name = 'videos'
urlpatterns = [
    path('', views.index, name="home"),
    path('video/<int:pk>', views.video_detail, name="video-detail")
]
