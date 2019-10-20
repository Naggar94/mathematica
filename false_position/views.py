from django.shortcuts import render
from sympy import *
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application
from false_position.calculations import false_position
from decimal import Decimal

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def submit(request):
	data = false_position(request.POST['equation'],Decimal(request.POST['maxval']),Decimal(request.POST['minval']),Decimal(request.POST['minval']),int(request.POST['iterations']),0,[])
	#data = [{'iteration':0,'xu':1.7,'xl':1.8,'xr':0.3}];
	print("Holloa")
	print(data)
	return render(request, 'index.html', {'data':data})