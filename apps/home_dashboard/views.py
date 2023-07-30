from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def display_home(request):

    return render(request, "index.html")
    # return HttpResponse('This is the home page')
