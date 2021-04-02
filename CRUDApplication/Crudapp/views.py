from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse
from .serializers import UserSerializer,UserSerializer1
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import *
import sys

def index(request):
    if request.method == 'GET':
        user=User.objects.all()
        return render(request, 'Crudapp/index.html',
                      {'user':user})

class Crud(generics.GenericAPIView):
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        original_stdout = sys.stdout
        print(request.data, original_stdout, '+++++++++++')
        id=request.GET.get('id')
        if id:
            try:
                user=User.objects.get(id=id)
                return Response({
                    "data": self.serializer_class(user).data,
                })
            except:
                return Response(
                    data={
                        "message": "Please pass a valid id",
                        "success": False
                    }, status=status.HTTP_403_FORBIDDEN
                )
        else:
            return Response(
                data={
                    "message": "Please pass id",
                    "success": False
                }, status=status.HTTP_403_FORBIDDEN
            )
    def post(self, request, *args):
        print(request.data)
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            print(request.data)
            user_serializer.save()
            return Response(
                data={
                    "data": user_serializer.data,
                    "message": "User saved successfully.",
                    "success": True,
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            data={
                "error":user_serializer.errors,
                "success": False,
            }, status=status.HTTP_404_NOT_FOUND
        )

    def put(self, request, *args):
        print(request.data)
        try:
            id = request.data['id']
            qs=User.objects.get(id=id)
            serializer = UserSerializer1(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.update(qs, request.data)
                print(serializer.data,'\\')
                return Response(
                    data={
                        "data": UserSerializer1(User.objects.get(id=id)).data,
                        "message": "User update successfully.",
                        "success": True,
                    }, status=status.HTTP_200_OK
                )
            except:
                return Response(
                    data={
                        "message": "Something Went Wrong.",
                        "success": False,
                    }, status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            print(e)
            return Response(
                data={
                    "message": "Please pass a valid id",
                    "success": False
                }, status=status.HTTP_403_FORBIDDEN
            )
    def delete(self, request, *args):

            id = request.data['id']
            if id:
                print('ldl', request.GET.get('id'), request.data['id'])
                try:
                    user = User.objects.get(id=id)
                    user.delete()
                    return Response(
                        data={
                         "message": "User deleted successfully",
                    })
                except:
                    print('lfl', request.GET.get('id'), request.data['id'])
                    return Response(
                        data={
                            "message": "Please pass a valid id",
                            "success": False
                        }, status=status.HTTP_403_FORBIDDEN
                    )
            else:
                print('lgl', request.GET.get('id'), request.data['id'])
                return Response(
                    data={
                        "message": "Please pass id",
                        "success": False
                    }, status=status.HTTP_403_FORBIDDEN
                )

class UserUpdate(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):


        id = request.GET.get('id')
        if id:
            try:
                user = User.objects.get(id=id)
                return Response({
                    "data": self.serializer_class(user).data,
                })
            except:
                return Response(
                    data={
                        "message": "Please pass a valid id",
                        "success": False
                    }, status=status.HTTP_403_FORBIDDEN
                )
        else:
            return Response(
                data={
                    "message": "Please pass id",
                    "success": False
                }, status=status.HTTP_403_FORBIDDEN
            )

def logs(request):
    log = Log.objects.all()
    return render(request, 'Crudapp/log.html',
                  {'log': log})