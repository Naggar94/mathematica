from django.shortcuts import render
from sympy import *
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application
from false_position.calculations import *
from decimal import Decimal
from django.http import HttpResponse
from false_position.KruskalGraph import *
from false_position.BrouvkaGraph import *
from false_position.DijkstraGraph import *
from random import randint

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

def kruskal_index(request):
    return render(request, 'kruskal_index.html', {})

def kruskal_submit(request):
	g = KruskalGraph(int(request.POST['nodes'])) 
	edges = []
	edgesCount = 1
	while (True):
		if 'edge['+str(edgesCount)+'][from_node]' in request.POST:
			edges.append({'from_node': request.POST['edge['+str(edgesCount)+'][from_node]'],'to_node': request.POST['edge['+str(edgesCount)+'][to_node]'],'weight': request.POST['edge['+str(edgesCount)+'][weight]']})
			g.addEdge(int(request.POST['edge['+str(edgesCount)+'][from_node]']), int(request.POST['edge['+str(edgesCount)+'][to_node]']), int(request.POST['edge['+str(edgesCount)+'][weight]'])) 
		else:
			break
		edgesCount = edgesCount + 1
	#return HttpResponse(g.KruskalMST())
	nodes = []
	nodesCount = int(request.POST['nodes'])
	while nodesCount > 0:
		nodes.append({'id':str(nodesCount-1),'xpos':randint(0, 100),'ypos':randint(0, 100)})
		nodesCount = nodesCount - 1
	mstResult = g.KruskalMST()
	print(mstResult)
	return render(request, 'kruskal_index.html', {'data':mstResult['response'],'nodes':nodes,'oldgraph':edges,'detailedSteps':mstResult['detailedSteps']})

def brouvka_index(request):
    return render(request, 'brouvka_index.html', {})

def brouvka_submit(request):
	g = BrouvkaGraph(int(request.POST['nodes'])) 
	edges = []
	edgesCount = 1
	while (True):
		if 'edge['+str(edgesCount)+'][from_node]' in request.POST:
			edges.append({'from_node': request.POST['edge['+str(edgesCount)+'][from_node]'],'to_node': request.POST['edge['+str(edgesCount)+'][to_node]'],'weight': request.POST['edge['+str(edgesCount)+'][weight]']})
			g.addEdge(int(request.POST['edge['+str(edgesCount)+'][from_node]']), int(request.POST['edge['+str(edgesCount)+'][to_node]']), int(request.POST['edge['+str(edgesCount)+'][weight]'])) 
		else:
			break
		edgesCount = edgesCount + 1
	#return HttpResponse(g.brouvkaMST())
	nodes = []
	nodesCount = int(request.POST['nodes'])
	while nodesCount > 0:
		nodes.append({'id':str(nodesCount-1),'xpos':randint(0, 100),'ypos':randint(0, 100)})
		nodesCount = nodesCount - 1
	return render(request, 'brouvka_index.html', {'data':g.boruvkaMST(),'nodes':nodes,'oldgraph':edges})

def dijkstra_index(request):
	# Driver program 
	g = DijkstraGraph(9) 
	g.addEdge(1,0,4)
	g.addEdge(7,0,8)
	g.addEdge(0,1,4)
	g.addEdge(2,1,8)
	g.addEdge(7,1,11)
	g.addEdge(1,2,8)
	g.addEdge(3,2,7)
	g.addEdge(5,2,4)
	g.addEdge(8,2,2)
	g.addEdge(2,3,7)
	g.addEdge(4,3,9)
	g.addEdge(5,3,14)
	g.addEdge(3,4,9)
	g.addEdge(5,4,10)
	g.addEdge(2,5,4)
	g.addEdge(3,5,14)
	g.addEdge(4,5,10)
	g.addEdge(6,5,2)
	g.addEdge(5,6,2)
	g.addEdge(7,6,1)
	g.addEdge(8,6,6)
	g.addEdge(0,7,8)
	g.addEdge(1,7,11)
	g.addEdge(6,7,1)
	g.addEdge(8,7,1)
	g.addEdge(2,8,2)
	g.addEdge(6,8,6)
	g.addEdge(7,8,7)
	# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
	#         [4, 0, 8, 0, 0, 0, 0, 11, 0], 
	#         [0, 8, 0, 7, 0, 4, 0, 0, 2], 
	#         [0, 0, 7, 0, 9, 14, 0, 0, 0], 
	        # [0, 0, 0, 9, 0, 10, 0, 0, 0], 
	        # [0, 0, 4, 14, 10, 0, 2, 0, 0], 
	        # # [0, 0, 0, 0, 0, 2, 0, 1, 6], 
	        # [8, 11, 0, 0, 0, 0, 1, 0, 7], 
	        # [0, 0, 2, 0, 0, 0, 6, 7, 0] 
	        # ]; 
	return HttpResponse(g.dijkstra(0))
    #return render(request, 'brouvka_index.html', {})
