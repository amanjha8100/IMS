from django.urls import path,include
from . import views

urlpatterns = [
    path('dashboard/',views.index,name="index"),
    path('staff/',views.staff,name="staff"),
    path('product/',views.product,name="product"),
    path('product/delete/<int:pk>',views.dele,name="delete"),
    path('product/edit/<int:pk>',views.edit,name="edit"),
    path('order/',views.order,name="order"),
]