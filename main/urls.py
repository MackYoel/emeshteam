from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/login/$', views.LoginHandler.as_view(), name='LoginHandler'),
    url(r'^accounts/logout/$', views.logout_handler, name='logout_handler'),
    url(r'^almuerzos/$', views.lunch, name='lunch'),
    url(r'^generate-score/$', views.generate_score, name='generate_score'),
]
