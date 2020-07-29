from django.shortcuts import render
from .models import User
from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from .models import Userpics
from django.shortcuts import render,redirect
from .forms import userpicsform


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        cuser = get_object_or_404(Userpics, user=request.user.username)

        return render(request,'dashboard.html',{'cuser':cuser})
    else:
        return render(request, 'dashboard.html',)


def userpics(request):

    if request.method == "POST":
        form = userpicsform(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("pages:index")
            except:
                pass
        else:
            return render(request, 'accounts/form.html', {'form': form})
    else:
        form = userpicsform()
        return render(request, 'accounts/form.html', {'form': form})