from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from manager.models import Book


def hello(request, digit=None):
    if digit is not None:
        return HttpResponse(f"hello is {digit}")
    return HttpResponse("hello world")


class MyPage(View):
    def get(self, request):
        context = {"books": Book.objects.all()}
        return render(request, "index.html", context)

# Create your views here.
