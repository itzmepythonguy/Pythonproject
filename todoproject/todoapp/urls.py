from django.urls import path
from . import views

app_name='todoapp'

urlpatterns=[
    path('',views.Home,name='Home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:fieldid>/',views.update,name='update'),
    path('listview/',views.listview.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.detailviews.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.updateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.deleteview.as_view(),name='deleteview'),

]