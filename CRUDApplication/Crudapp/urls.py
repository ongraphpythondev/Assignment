from django.urls import path
from . import views


# app_name = 'campaign'
urlpatterns = [

    path('',views.index,name='index'),
    path('cruds/',views.Crud.as_view(),name='crud'),
    path('log/',views.logs,name='log'),
    # path('users/', views.UserList.as_view(),name='crud'),
    # path('users/<int:pk>/', views.UserRetrieveUpdateDelete.as_view(),name='crud1'),
    path('user-update/',views.UserUpdate.as_view(),name='user-update'),
]
