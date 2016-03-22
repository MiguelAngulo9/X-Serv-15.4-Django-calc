from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request, numero1, numero2):
    resultado = int(numero1) + int(numero2)
    return HttpResponse('El resultado es ' + str(resultado))

def resta(request, numero1, numero2):
    resultado = int(numero1) - int(numero2)
    return HttpResponse('El resultado es ' + str(resultado))

def multiplicacion(request, numero1, numero2):
    resultado = int(numero1) * int(numero2)
    return HttpResponse('El resultado es ' + str(resultado))

def division(request, numero1, numero2):
    resultado = int(numero1) / int(numero2)
    return HttpResponse('El resultado es ' + str(resultado))

def ElError404(request):
    return HttpResponse('<h1><font color="red">Not Found!</font></h1>')
