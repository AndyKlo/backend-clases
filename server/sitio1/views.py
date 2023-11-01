from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Venta, DetalleVenta, Producto


def index(request):
    return render(request, "sitio1/ver_productos.html")

def contacto(request):
    return render(request, "sitio1/contacto.html", {})

def carrito(request):
    return HttpResponse("carrito")

#def usuario(request):
    datos = {"datos":{"nombre":"Andy","apellido":"Mellado"}}
    montos = {"datos":[1,23,456,78,654,321]}

    usu = Usuario.objects.all()
    venta = Venta.objects.all()
    context = {"datos":venta}
    return render(request, "sitio1/index.html", context)

def detalleVenta(request):
    datosDetalle = DetalleVenta.objects.all()
    context = {'datos':datosDetalle}
    return render(request, "ver_productos/index.html", context)

#PRODUCTOS

def productos_add(request, id):
    pass
def productos_edit(request):
    productos = Producto.objects.filter(id = id and Producto.eliminado == False)
    if request.method == "POST":
        print(id, "POST")
        
def productos_del(request):
    pass

def productos_list(request):
    productos = Producto.objects.all()
    print(productos)
    return render(request, "sitio1/ver_productos.html", {"datos":productos})
