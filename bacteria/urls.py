from django.urls import path
from .views import HomePageView, ReturnPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home.html'),
    path('return/', ReturnPageView.as_view(), name='return'),
]