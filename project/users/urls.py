from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile', views.user_profile, name="profile"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^thanks', views.thanks, name="thanks"),
    url(r'^contact', views.contact, name="contact"),
    url(r'^sell$', views.sell, name="sell"),
    url(r'^category/(?P<category_name>[\w-]*)/$', views.category, name='category'),
    url(r'^selldone',views.selldone, name="selldone"),
    url(r'^item/(?P<item_id>[\d-]*)/$',views.item, name='item'),
    url(r'^index/',views.index,name='index'),
    url(r'^search',views.search, name='search'),
    url(r'^logout',views.logout, name='logout'),
    url(r'^login',views.login_view, name='login_view'),
]
