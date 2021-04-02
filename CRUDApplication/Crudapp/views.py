from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.forms.models import model_to_dict

class GetUserApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer()
    # lookup_field = 'pk'
    def get(self,request,id):
        # import pdb;pdb.set_trace()
        try:
            try:
                # u = User.objects.get(id=id).values_list('username')
                u=User.objects.values('username','first_name','last_name','email').get(pk=id)
                # data=model_to_dict(u)
                return JsonResponse({'success': True,'data':u})
            except:
                return JsonResponse({'success': False, 'message': 'User Does not exist'},status=status.HTTP_400_BAD_REQUEST)
        except:
            pass

class UserCreateApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteApi(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

