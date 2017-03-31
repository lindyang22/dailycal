from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
import csv


# Create your views here.

def index(request):
	template = loader.get_template('interactivechart/graphic.html')
	return HttpResponse(template.render(request))

def applied(request):
	return HttpResponse.read("static/applieddata2.csv")

def admitted(request):
	return "static/admitteddata2.csv"

def SIRed(request):
	return "static/SIRed.csv"

# def user_selection_filter(request, ethnicity, gender, location, college):
	"""use these values from a drop down menu to grab the data"""
