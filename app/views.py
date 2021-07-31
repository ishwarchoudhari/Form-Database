from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Students
from .models import User


# Create your views here.
def index(request):
    if request.method == 'POST':
        data = Students(request.POST)
        if data.is_valid():
            print("From Validate")
            name = data.cleaned_data['name']
            email = data.cleaned_data['email']
            password = data.cleaned_data['password']
            reg = User(name = name, email = email, password = password)
            
            reg.save()
            re = User.objects.all()
            # rpassword = data.cleaned_data['rpassword']
            print('Name:', name)
            print('E-mail:', email)
            print('Password:', password)
            # print('Confirm Password:',rpassword)
            # return HttpResponseRedirect('/done/')
            return render(request, 'done.html', {'re': re })
    else:
        data = Students()

    return render(request, 'home.html', {'form': data})
