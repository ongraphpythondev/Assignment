"""CRUDApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from Crudapp.views import CreateCrudUser, DeleteCrudUser, UpdateCrudUser

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('crud/list', CrudView.as_view(), name='crud_list'),
    path('crud/create/', CreateCrudUser.as_view(), name='crud_create'),
    path('crud/delete/', DeleteCrudUser.as_view(), name='crud_delete'),
    path('crud/update/', UpdateCrudUser.as_view(), name='crud_update'),

]
