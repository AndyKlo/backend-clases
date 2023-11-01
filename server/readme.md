python pip -m install django
django-admin startproject server ( creo la carpeta dentro de la ruta que yo escoja) 

python manage.py startapp sitio1
Para crear una vista necesito importar: 
from django.http import HttpResponse
dentro de la carpeta "view"
dentro de view escribo:
def index(request):
    return HttpResponse("holaMundo")
