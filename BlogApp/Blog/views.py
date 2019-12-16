from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>BLOG HOMEPAGE</h1>')

def about(request):
	return HttpResponse('<h1>ABOUT BLOG</h1>')