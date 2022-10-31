from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from .models import Task

class LoginFormView(LoginView):
	template_name = 'todos/login.html'
	# redirect_field_name = reverse_lazy('todos:index')
	next_page = reverse_lazy('todos:index')

class LogoutFormView(LogoutView):
	# redirect_field_name = reverse_lazy('todos:index')
	next_page = reverse_lazy('todos:login')

def indexView(request):
	obj = Task.objects.all()
	return render(request, "todos/index.html", {"todo_list": obj})

def createView(request):
	if request.method == 'POST':
		new_task = request.POST['tname']

		if new_task:
			obj = Task(task_description=new_task)
			obj.save()

	return HttpResponseRedirect(reverse('todos:index'))

def deleteView(request, task_id):
	obj = Task.objects.get(id=task_id)
	obj.delete()

	return HttpResponseRedirect(reverse('todos:index'))

def updateView(request, task_id):
	if request.method == 'POST':
		obj = Task.objects.get(id=task_id)
		new_desc = request.POST['newtask']
		print(new_desc)
		if len(new_desc) > 0:
			obj.task_description = new_desc
			obj.save()

			return HttpResponseRedirect(reverse('todos:index'))

	obj = Task.objects.all()
	edit_obj = Task.objects.get(id=task_id)
	return render(request, "todos/todos_update.html", {"todo_list": obj, "todo_edit": edit_obj})
