from sympy import *
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application

def false_position(equation,xu,xl,xr,iterations,trial,response):
	print("trial")
	print(trial)
	if iterations == 0:
		return response

	xrold = xr
	x = symbols('x')
	transformations = (standard_transformations +(implicit_multiplication_application,))
	expr = parse_expr(equation,transformations=transformations)
	es = 0.00001
	fu = expr.evalf(subs={x:xu})
	fl = expr.evalf(subs={x:xl})
	xr = xu - (fu * ((xl-xu)/(fl-fu)))
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