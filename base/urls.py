from django.contrib import admin
from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,Taskupdate,Tasklogin,TaskDelete,Taskregister
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('',TaskList.as_view(),name='home'),
   path('detail/<int:pk>/',TaskDetail.as_view(),name='detail'),
   path('create/',TaskCreate.as_view(),name='create'),
   path('update/<int:pk>/',Taskupdate.as_view(),name='update'),
   path('delete/<int:pk>/',TaskDelete.as_view(),name='delete'),
   path('login/',Tasklogin.as_view(),name='login'),
   path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
   path('register/',Taskregister.as_view(),name='register'),
]