from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from .models import Producto, Proveedor
from .forms import ProveedorRegisterForm, ProductoRegisterForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'compra/index.html'

class ListadoProductos(ListView):
    template_name = "compra/listado_productos.html"
    model = Producto
    context_object_name = "productos"

class ListadoProveedores(ListView):
    template_name = "compra/listado_proveedores.html"
    model = Proveedor
    context_object_name = "proveedores"

class CreateProveedor(CreateView):
    template_name = "compra/agregar_proveedor.html"
    model = Proveedor
    form_class = ProveedorRegisterForm
    success_url = reverse_lazy('compra_app:listado_productos')

class CreateProducto(CreateView):
    template_name = "compra/agregar_producto.html"
    model = Producto
    form_class = ProductoRegisterForm
    success_url = reverse_lazy('compra_app:listado_productos')