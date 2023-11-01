from django.contrib import admin

# Register your models here.
from sitio1.models import Usuario
from sitio1.models import Producto

admin.site.register(Usuario)
admin.site.register(Producto)