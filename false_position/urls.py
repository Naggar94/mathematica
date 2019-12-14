from django.urls import path
from false_position import views

urlpatterns = [
    path('false-position/', views.false_point_index, name='false-position-index'),
    path('false-position/submit/', views.false_point_submit, name='false-position-submit'),
    path('secant/', views.secant_index, name='secant-index'),
    path('secant/submit/', views.secant_submit, name='secant-submit'),
    path('kruskal/', views.kruskal_index, name='kruskal-index'),
    path('kruskal/submit/', views.kruskal_submit, name='kruskal-submit'),
    path('brouvka/', views.brouvka_index, name='brouvka-index'),
    path('brouvka/submit/', views.brouvka_submit, name='brouvka-submit'),
    path('dijkstra/', views.dijkstra_index, name='dijkstra-index'),
]