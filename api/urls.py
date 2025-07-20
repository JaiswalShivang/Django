from django.contrib import admin
from django.urls import path,include
from api.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
  
urlpatterns = [
    path('',index,name="indexpage"),
    path('signup/',signuppage,name="signup"),
    path('login/',loginpage,name="login"),
    path('logout/',logoutpage,name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()