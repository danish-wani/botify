from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import UserLogin, Home


app_name = 'user'


urlpatterns = [
    path('', login_required(Home.as_view()), name='home'),
    path('login', UserLogin.as_view(), name='user_login'),
    path('v1/', include('user.apis.rest.endpoints'))
]
