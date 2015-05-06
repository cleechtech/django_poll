from django.conf.urls import patterns, include, url
from rest_framework import routers
from resume.api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users', views.GroupViewSet)

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(router.urls)),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework'))
)
