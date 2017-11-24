from django.conf.urls import url
from django.contrib import admin
from posts.views import(
    post_create,
    post_retreive,
    post_delete,
    post_list,
    post_update,

)
urlpatterns = [
    url(r'^$' , post_list , name="list"),
    url(r'^create/$' , post_create),
    url(r'^retrieve/(?P<id>\d+)/$' , post_retreive , name="detials"),
    url(r'^(?P<id>\d+)/delete/$' , post_delete ,  name="delete"),
    url(r'^(?P<id>\d+)/edit$' , post_update  , name="update"),
]
