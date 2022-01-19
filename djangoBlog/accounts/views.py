from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm

def accounts(request):
    return HttpResponse('<b>accounts page</b>')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #login
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})
