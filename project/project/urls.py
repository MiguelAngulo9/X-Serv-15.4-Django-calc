from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'pep[ae]\d*$', 'miapp.views.mifuncion'),
    #url(r'(\d+)+(\d+)/$', 'miapp.views.suma'),
    url(r'(?P<numero1>\d+)\+(?P<numero2>\d+)', 'calc.views.suma'),
    #Pongo la barra antes del +, pues asi hago referencia a varias cosas (si no la pongo da error)
    url(r'(?P<numero1>\d+)\-(?P<numero2>\d+)', 'calc.views.resta'),
    url(r'(?P<numero1>\d+)\*(?P<numero2>\d+)', 'calc.views.multiplicacion'),
    url(r'(?P<numero1>\d+)\/(?P<numero2>\d+)', 'calc.views.division'),
    url(r'.*', 'calc.views.ElError404')
]
