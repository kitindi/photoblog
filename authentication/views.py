from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create login views here.

def login_page(request):
    form = LoginForm()
    message =''
    context = {'form': LoginForm}
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
              login(request,user)
              return redirect('home')
         
                     
    return render(request, 'authentication/login.html', context )


# create logout view

def logout_user(request):
    logout(request)
    return redirect('login')

# create signup view 

