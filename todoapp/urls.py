from django.urls import path,include
from .import views

urlpatterns = [
    
     path('',views.ABC,name="ABC"),
     path('delete/<int:id>/',views.delete,name="delete"),
     path('update/<int:id>/',views.update,name="update"),
     path('cbv/',views.Tasklistview.as_view(),name='cbv'),
     path('cbd/<int:pk>/',views.Taskdetailview.as_view(),name="cbd"),
     path('cbu/<int:pk>/',views.Taskupdate.as_view(),name="cbu"),
     path('cbt/<int:pk>/',views.Taskdelete.as_view(),name="cbt"),

]
