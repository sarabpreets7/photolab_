from django.shortcuts import render,redirect,reverse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsersSerializer

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are logged in!')
            return redirect('pages:index')

    return render(request,'accounts/login.html')


def logout(request):

    auth.logout(request)
    messages.success(request,'Logged out')
    return redirect('pages:index')





def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username taken ')
                return redirect('accounts:register')

            else:

                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email taken ')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    messages.success(request,'User created!')
                    return redirect('pages:index')



        else:
            messages.error(request,'Passwords do not match')
            return redirect('accounts:register')
    else:

        return render(request, 'accounts/register.html')



class userslist(APIView):

    def get(self,request):
        users = User.objects.all()
        serializer = UsersSerializer(users,many=True)
        return Response(serializer.data)

    def post(self):
        pass