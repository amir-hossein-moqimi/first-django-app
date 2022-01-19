from django.shortcuts import render
# from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hi there!')
    return render(request, 'about.html')

def home(request):
    # return HttpResponse('here is home')
    return render(request, 'Home.html')