from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Task

class LoginFormView(LoginView):
	template_name = 'todos/login.html'
	next_page = reverse_lazy('todos:index')

class LogoutFormView(LogoutView):
	next_page = reverse_lazy('todos:login')

@login_required(login_url=reverse_lazy('todos:login'))
def indexView(request):
	obj = Task.objects.filter(user=request.user)

	return render(request, "todos/index.html", {"todo_list": obj})

@login_required(login_url=reverse_lazy('todos:login'))
def createView(request):
	if request.method == 'POST':
		new_task = request.POST['tname']

		if new_task:
			obj = Task(description=new_task, user=request.user)
			obj.save()

	return HttpResponseRedirect(reverse('todos:index'))

@login_required(login_url=reverse_lazy('todos:login'))
def deleteView(request, task_id):
	obj = Task.objects.get(id=task_id)
	obj.delete()

	return HttpResponseRedirect(reverse('todos:index'))

@login_required(login_url=reverse_lazy('todos:login'))
def updateView(request, task_id):
	if request.method == 'POST':
		obj = Task.objects.get(id=task_id)
		new_desc = request.POST['newtask']

		if len(new_desc) > 0:
			obj.description = new_desc
			obj.save()

			return HttpResponseRedirect(reverse('todos:index'))

	obj = Task.objects.filter(user=request.user)
	edit_obj = Task.objects.get(id=task_id)
	return render(request, "todos/todos_update.html", {"todo_list": obj, "todo_edit": edit_obj})
