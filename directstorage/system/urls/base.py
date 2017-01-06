from django.conf.urls import url
from system import views
from django.contrib.auth import get_user_model

User = get_user_model()

base_urlpatterns = (
    url(r'^me/$', views.UserView.as_view(), name='user'),
)

urlpatterns = base_urlpatterns
