
from django.urls import path,include
from  app1 import views
urlpatterns = [
    
    path('',views.todo,name='todo'),
    path('delet/<str:pk>/',views.delet,name='delet'),
]