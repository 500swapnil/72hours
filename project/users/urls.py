from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile', views.user_profile, name="profile"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^thanks', views.thanks, name="thanks"),
]
