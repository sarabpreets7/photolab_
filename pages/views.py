from django.shortcuts import render
from django.shortcuts import render
from user.models import User
from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from user.models import Userpics
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated and Userpics.objects.filter(user=request.user.username).exists():
        cuser = get_object_or_404(Userpics, user=request.user.username)

        return render(request, 'pages/index.html', {'cuser': cuser})



    else:
        return render(request, 'pages/index.html', )

def category(request):
    return render(request,'pages/category.html')


def contact(request):
    return render(request,'pages/contact.html')

def about(request):

    return render(request,'pages/about.html')