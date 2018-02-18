from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^users/(?P<uid>\d+)/$', views.show),
  url(r'^users/create/$', views.create),
  url(r'^users/new/$', views.new),
  url(r'^users/$', views.index)     # This line has changed!
]
