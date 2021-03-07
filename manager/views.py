from django.http import HttpResponse
from django.shortcuts import render


def hello(request, digit=None):
    if digit is not None:
        return HttpResponse(f"hello is {digit}")
    return HttpResponse("hello world")


# Create your views here.
