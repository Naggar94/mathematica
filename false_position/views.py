from django.shortcuts import render
from sympy import *
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application
from false_position.calculations import *
from decimal import Decimal

# Create your views here.
def false_point_index(request):
    return render(request, 'index.html', {})

def false_point_submit(request):
	data = false_position(request.POST['equation'],Decimal(request.POST['maxval']),Decimal(request.POST['minval']),Decimal(request.POST['minval']),int(request.POST['iterations']),0,[])
	#data = [{'iteration':0,'xu':1.7,'xl':1.8,'xr':0.3}];
	if data == None:
		return render(request, 'index.html', {'error':'1'})
	return render(request, 'index.html', {'data':data})

def secant_index(request):
    return render(request, 'secant_index.html', {})

def secant_submit(request):
	data = secant(request.POST['equation'],Decimal(request.POST['maxval']),Decimal(request.POST['minval']),Decimal(request.POST['maxval']),0,int(request.POST['iterations']),0,[])
	#data = [{'iteration':0,'xu':1.7,'xl':1.8,'xr':0.3}];
	if data == None:
		return render(request, 'secant_index.html', {'error':'1'})
	return render(request, 'secant_index.html', {'data':data})