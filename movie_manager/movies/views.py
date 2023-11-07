from django.shortcuts import render,redirect
from . models import MovieInfo
from . forms import MovieForm

def index(request):
    return render(request,'index.html')

def create(request):
    frm = MovieForm()
    if request.POST:
        frm = MovieForm(request.POST)
        if frm.is_valid:
            frm.save()
            return redirect('list')
    return render(request,'create.html',{'frm' : frm})

def lists(request):
    movie_set = MovieInfo.objects.all()
    return render(request,'list.html',{'movies' : movie_set })

def edit(request,pk):
    instance_edit = MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm = MovieForm(request.POST,instance = instance_edit)
        if frm.is_valid():
            instance_edit.save()
            return redirect('list')
    else:
        frm = MovieForm(instance = instance_edit)
    return render(request,'create.html',{'frm' : frm})

def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()
    return render(request,'list.html',{'movies' : movie_set })
