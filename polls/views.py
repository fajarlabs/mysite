from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
   loginTitle = "Login Page"
   return render(request, "myapp/login.html", {"loginTitle" : loginTitle})

def hello(request):
   today = datetime.datetime.now().date()
   return render(request, "myapp/hello.html", {"today" : today})

def morning(request):
   text = """<h1>welcome morning !</h1>"""
   return HttpResponse(text)

def viewArticle(request, articleId):
   text = "Displaying article Number : %s" % articleId
   return HttpResponse(text)

def viewArticles(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)

def page_redirect(request):
	return redirect(viewArticles, "20", "17")