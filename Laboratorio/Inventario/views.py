from django.shortcuts import render, redirect
from .models import Reactivo
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages

# Create your views here.
def home(request):
    reactivos = Reactivo.objects.all()
    
    return render(request, "gestionInv.html", {"reactivos": reactivos})

@requires_csrf_token
def registrarInv(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    cantidad=request.POST['numCantidad']

    invEntry = Reactivo.objects.create(
        codigo=codigo, nombre=nombre, cantidad=cantidad
    )

    return redirect('/')

def deleteInv(request, codigo):

    invEntry = Reactivo.objects.get(codigo=codigo)
    invEntry.delete()
    messages.success(request, 'Lote eliminado')
    return redirect('/')

 

def editInventory(request, codigo):
    invEntry = Reactivo.objects.get(codigo=codigo)
    return render(request, "editInventory.html", {"invEntry":invEntry})

def editEntry(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    cantidad=request.POST['numCantidad']

    
    invEntry = Reactivo.objects.get(codigo=codigo)

    invEntry.nombre = nombre
    invEntry.cantidad = cantidad
    invEntry.save()

    
    return redirect('/')


