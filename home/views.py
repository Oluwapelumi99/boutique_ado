from django.shortcuts import render

# Create your views here.


def index(reqest):
    """ A view to retur the index page """
    return render (reqest, 'home/index.html')