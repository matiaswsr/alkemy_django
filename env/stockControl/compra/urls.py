from django.urls import path
from . import views

app_name = 'compra_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('listado_productos', views.ListadoProductos.as_view(), name="listado_productos"),
    path('listado_proveedores', views.ListadoProveedores.as_view(), name="listado_proveedores"),
    path('agregar_proveedor', views.CreateProveedor.as_view(), name="agregar_proveedor"),
    path('agregar_producto', views.CreateProducto.as_view(), name="agregar_producto"),   
]