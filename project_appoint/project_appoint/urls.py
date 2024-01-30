"""
URL configuration for project_appoint project.

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.Base.as_view(),name='base'),
    path('appoint/',views.Appoint.as_view(),name='appoint'),
    path('show/',views.show,name='show'),
    path('doctor/',views.Doctor,name='doctor'),
    path('done/<int:id>',views.History,name='done'),
    path('doctsignup/',views.Doc_SignUp,name='doctsignup'),
    path('doctlogin/',views.Doc_Login,name= 'doctlogin'),
    path('',views.User_SignUp,name='usersignup'),
    path('userlogin/',views.User_Login,name='userlogin'),
    path('userlogout/',views.User_Logout,name='userlogout')
]
