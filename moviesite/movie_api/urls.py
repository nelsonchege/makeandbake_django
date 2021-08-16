from django.urls import path
from .views import WatchListAV,DetailsAV,StreamingPlatformAV,SingleStreamingPlatformAV,ReviewList,ReviewDetail

urlpatterns = [
    path('watch_list/', WatchListAV.as_view()),
    path('single_watch/<int:pk>/', DetailsAV.as_view()),
    path('stream_list/', StreamingPlatformAV.as_view()),
    path('single_stream/<int:pk>/', SingleStreamingPlatformAV.as_view()),
    path('review/', ReviewList.as_view()),
    path('review/<int:pk>/', ReviewDetail.as_view())
]