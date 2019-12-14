from sympy import *
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application
import math

def false_position(equation,xu,xl,xr,iterations,trial,response):
	if iterations == 0:
		return response

	xrold = xr
	x = symbols('x')
	transformations = (standard_transformations +(implicit_multiplication_application,))
	expr = parse_expr(equation,transformations=transformations)
	es = 0.00001
	fu = expr.evalf(subs={x:xu})
	fl = expr.evalf(subs={x:xl})
	if trial == 0:
		if fu*fl > 0:
			return None
	xr = xu - (fu * ((xl-xu)/(fl-fu)))

	if math.isnan(xr):
		return response

	fr = expr.evalf(subs={x:xr})
	test = fl * fr
	if test < 0:
		xu = xr
	elif test > 0:
		xl = xr
	else :
		return [{'iteration':trial,'xu':xu,'xl':xl,'xr':xr}]

	ea = abs((xr-xrold)/xr)*100

	if ea < es :
		return [{'iteration':trial,'xu':xu,'xl':xl,'xr':xr}]

	response = false_position(equation,xu,xl,xr,iterations-1,trial+1,[])
	response.append({'iteration':trial,'xu':xu,'xl':xl,'xr':xr})
	return response

def secant(equation,x1,x0,xr,fr,iterations,trial,response):
	if iterations == 0:
		return response

	xrold = xr
	x = symbols('x')
	transformations = (standard_transformations +(implicit_multiplication_application,))
	expr = parse_expr(equation,transformations=transformations)
	es = 170000
	fu = expr.evalf(subs={x:x1})
	fl = expr.evalf(subs={x:x0})
	xr = x1 - (fu * ((x0-x1)/(fl-fu)))
	newfr = expr.evalf(subs={x:xr})

	if math.isnan(xr):
		return response

	if trial > 0 and abs(newfr) > abs(fr):
		return None

	if newfr == 0.0 :
		return [{'iteration':trial,'xr':xr,'fr':newfr}]

	ea = abs((xr-xrold)/xr)*100

	if ea > es :
		return [{'iteration':trial,'xr':xr,'fr':newfr}]

	response = secant(equation,xr,x1,xr,newfr,iterations-1,trial+1,[])
	if response == None:
		return None
	response.append({'iteration':trial,'xr':xr,'fr':newfr})
	return response
