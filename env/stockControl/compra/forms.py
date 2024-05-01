from django import forms
from .models import Proveedor, Producto

class ProveedorRegisterForm(forms.ModelForm):   

    class Meta:
        model = Proveedor
        # Indicamos que atributos del modelo queremos ver en el HTML        
        fields = (
            'nombre',
            'apellido',
            'dni',
        )

class ProductoRegisterForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = (
            'proveedor',
            'nombre',
            'precio',
            'stock_actual'
        )        
    
        widgets = {
            'proveedor': forms.Select(
                    attrs = {
                        'class': 'form-control',
                    }
                ),
            }
