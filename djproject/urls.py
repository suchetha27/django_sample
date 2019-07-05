"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

#from account import views
from account.views import home_view,user_login,register,user_logout
#from home.views import home_view,contact,about,deletestudent,editstudent,createstudent
#from home import views

urlpatterns = [
    #path('',views.home_view)
    path('home/',include('home.urlsh')),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
    path('admin/', admin.site.urls),
    #path('',views.home_view),#it is for from home import views
    path('',home_view,name='home'),
    # path('home/',include('home.urlsh')),
    #path('contact/',contact),
    #path('about/',about),
    # path('admin/', admin.site.urls),
    #path('delete-student/<id>',deletestudent),
    #path('create-student/',createstudent),
    #path('edit-student/<id>',editstudent)
]