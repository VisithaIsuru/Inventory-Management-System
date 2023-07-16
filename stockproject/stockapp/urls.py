from django.urls import path
from stockapp import views

urlpatterns = [
    path('', views.index, name='stockapp-index'),
    path('item/', views.item, name='stockapp-item'),
    path('staff/', views.staff, name='stockapp-staff'),
    path('staff/details/<int:pk>/', views.staff_details, name='stockapp-staff-details'),
    path('item/delete/<int:pk>/', views.item_delete, name='stockapp-item-delete'),
    path('item/update/<int:pk>/', views.item_update, name='stockapp-item-update'),
    path('report/', views.report, name='stockapp-report')
]