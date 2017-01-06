from django.conf.urls import url
from system import views
from . import base
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = base.base_urlpatterns + (
    url(r'^login/', obtain_jwt_token),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
)
