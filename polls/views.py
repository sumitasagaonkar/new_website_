from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	sumit= "amit"
	con={"nere" : sumit}
	return render(request, 'home2.html',con)