from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
	objs = Todo.objects.all()
	form = TodoForm()
	content ={
		"objects":objs,
		"form":form
	}
	if request.method=="POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect('/')
	return render(request, "todo/index.html",content)

def update(request, pk):
	updatedtodo = Todo.objects.get(id=pk)

	form = TodoForm(instance = updatedtodo)
	content = {
		'form':form
	}
	if request.method == "POST":
		form = TodoForm(request.POST,instance = updatedtodo)
		if form.is_valid():
			form.save()
		return redirect('/')
	return render(request,"todo/edit.html", content)


def delete(request, pk):
	item = Todo.objects.get(id = pk)
	content = {"item": item}
	if request.method=="POST":
		item.delete()
		return redirect('/')
	return	render(request, 'todo/delete.html', content)