from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This is about page')
def home2(request):
	return render (request, 'home2.html', {"guti1": "5674568745gdhdit"})
def home1(request):
	return render (request, 'home1.html', {"guti": "Privfgdhdit"})
def home(request):
	return HttpResponse('popka durak')