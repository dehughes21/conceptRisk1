from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from ProofOfConcept.forms import CreateForm
from .models import Squirrel

def home(request):
    return render(request, 'home/home.html', {'data' : 'HOME'})

def create(request):
    if request.POST:
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)

    return render(request, 'create/create.html', {'form' : CreateForm})

def read(request):
    data = Squirrel.objects.all()
    return render(request, 'read/read.html', {'squirrels' : data})

def detail(request, id):
    squirrel = Squirrel.objects.get(pk=id)
    if squirrel:
        return render(request, 'read/detail.html', {'squirrel' : squirrel})
    else:
        raise Http404('Squirrel does not exist')

def update(request):
    return render(request, 'update/update.html', {'data' : "UPDATE"})

def delete(request):
    return render(request, 'delete/delete.html', {'data' : "DELETE"})

