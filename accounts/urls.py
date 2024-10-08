"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers

app_name = "accounts"

urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
    path("api-token-auth/", auth_token.obtain_auth_token),
    path("userlist/", views.UserListView.as_view() , ),
]

router = routers.SimpleRouter()
router.register("user", views.UserViewSet)
urlpatterns += router.urls
