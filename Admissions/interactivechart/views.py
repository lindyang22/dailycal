from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
	return HTTPResponse("Hello")
	
def user_selection_filter(request, ethnicity, gender, location, college):
	"""use these values from a drop down menu to grab the data"""
