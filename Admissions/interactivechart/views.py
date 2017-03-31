from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
import csv
from . import models
from . import utils

# Create your views here.

def index(request):
	template = loader.get_template('interactivechart/index.html')
	return HttpResponse(template.render(request))

def filter(request):

	filter_applied = Student.objects.filter(status = "('Applied')")
	return render(request, 'interactivechart/graphic.html', {'all_applied': filter_applied})

"""def request_page(request):
	if request.method == 'GET':
	    form = YourForm(request.POST)
		if form.is_valid():
	      	answer = form.cleaned_data['value']
	return render(request,'interactivechart/graphic.html')"""

# def applied(request):
	# return open("interactivechart/applieddata2.csv")

# def admitted(request):
	# return "static/admitteddata2.csv"

# def SIRed(request):
	# return "static/SIRed.csv"

# def user_selection_filter(request, ethnicity, gender, location, college):
"""use these values from a drop down menu to grab the data"""
