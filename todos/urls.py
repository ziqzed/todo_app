from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutFormView.as_view(), name='logout'),
    path('create', views.createView, name='create'),
    path('delete/<int:task_id>', views.deleteView, name='delete'),
    path('update/<int:task_id>', views.updateView, name='update'),
]
