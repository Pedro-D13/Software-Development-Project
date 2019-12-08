from django.shortcuts import render
# Create your views here.


def homeview(request, *args, **kwargs):
    # homeview, will resolve the request and render the htmlpage
    return render(request, 'gymapp/homepage.html')
