from django.urls import path

from .views import SignUpView, About


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('about/', About.as_view(), name= 'about')
    
]