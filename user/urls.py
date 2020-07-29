from django.urls import path,include
from . import views
from user.views import userpics
app_name='user'

urlpatterns = [

    path('dashboard/',views.dashboard,name='dashboard'),
    path('userform/',userpics,name='userpics'),

]