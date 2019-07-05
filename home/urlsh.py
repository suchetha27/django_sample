from django.urls import path

from . views import *

urlpatterns = [
    path('',home_view,name='home'),
    path('delete-student/<id>',deletestudent),
    path('create-student/',createstudent),
    path('edit-student/<id>',editstudent),
]