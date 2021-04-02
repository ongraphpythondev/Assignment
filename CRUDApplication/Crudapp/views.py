from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse


class CreateCrudUser(View):
    def  get(self, request):
        username = request.GET.get('username', None)
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        email = request.GET.get('email', None)

        obj = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,

        )

        user = {'id':obj.id,'username':obj.username,'first_name':obj.first_name,'last_name':last_name}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        username = request.GET.get('username', None)
        first_name = request.GET.get('first_name', None)
        last_name = request.GET.get('last_name', None)
        email = request.GET.get('email', None)

        obj = User.objects.get(id=id1)
        obj.username = username
        obj.first_name = first_name
        obj.last_name = last_name
        obj.email=email
        obj.save()

        user = {'id':obj.id,'username':obj.username,'first_name':obj.first_name,'last_name':obj.last_name,'email':obj.email}

        data = {
            'user': user
        }
        return JsonResponse(data)





