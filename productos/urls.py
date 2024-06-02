from django.urls import path

from .views import listar_productos, agregar_producto, editar_producto, eliminar_producto

urlpatterns = [
    # URLs de vistas normales
    path('', listar_productos, name='listar_productos'),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('<id>/editar', editar_producto, name='editar_producto'),
    path('<id>/eliminar', eliminar_producto, name='eliminar_producto'),
]