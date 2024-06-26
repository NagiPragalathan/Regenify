"""
URL configuration for EchoAgri project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from base.Routes.Auth import *
from base.Routes.Home import *
from base.Routes.VideoConf import *
from base.Routes.Ocr import *

urlpatterns = []

AdminUrl = [
    path("admin/", admin.site.urls),
]
Auth = [
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
]
Home = [
    path('', home,name="home" )
]
video_conf_url = [
    path('MeetRoom',MeetRoom,name='MeetRoom'),
]
AiOCR = [
    path('show_doc', show_doc, name='show_doc'),
    path('file_to_txt', upload_image_view, name='file_to_txt'),
    path('get_bot_response', get_bot_response, name='get_bot_response'),
]


urlpatterns.extend(Home)
urlpatterns.extend(Auth)
urlpatterns.extend(video_conf_url)
urlpatterns.extend(AdminUrl)
urlpatterns.extend(AiOCR)
