from django.urls import path
from .import views

urlpatterns = [
    path("index", views.detalleVenta, name="index"),
    path("", views.index, name="index"),
    path("contacto", views.contacto, name="contacto"),
    #path("carrito", views.carrito, name="carrito"),

    #URLS PRODUCTO
    path("productos/crear", views.productos_add, name="pro_add"),
    path("productos/editar/<int:id>", views.productos_edit, name="pro_edit"),
    path("productos/eliminar", views.productos_del, name="pro_del"),
    path("productos/listar", views.productos_list, name="pro_list")

]
