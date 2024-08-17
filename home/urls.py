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
from home import views

app_name = "home"
urlpatterns = [
    path("home/", views.home, name="home"),
    path("homebase/", views.HomeView.as_view(), name="home"),
    path("nameparam/", views.NameParamsView.as_view(), name="nameparam"),
    # path("<str:name>/", views.NameView.as_view(), name="name"),
    path("homeser/", views.HomeSerializerView.as_view(), name="homeser"),
    # path("questions/", views.QuestionView.as_view(), name="questions"),
    path("questions/", views.QuestionListView.as_view(), name="questions"),
    path("question/creat/", views.QuestionCreatView.as_view(), name="creat_questions"),
    path("question/<int:pk>/", views.QuestionView.as_view(), name="questions_update"),
    path("question/update/<int:pk>/", views.QuestionUpdateView.as_view(), name="questions_update"),
    path("question/delete/<int:pk>/", views.QuestionDeleteView.as_view(), name="questions_delete"),
]
