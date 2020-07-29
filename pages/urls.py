from django.urls import path,include
from . import views
app_name='pages'

urlpatterns = [

    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('category/',views.category,name='category'),
    path('contact/',views.contact,name='contact'),
]