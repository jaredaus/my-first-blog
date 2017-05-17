from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #This regular expression will match ^ (a beginning) followed by $ (an end) – so only an empty string will match
]