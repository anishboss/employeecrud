from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('add_employee/',views.add_employee,name='add_employee'),
    path('edit/<int:id>',views.edit_employee,name='edit_employee'),
    path('delete/<int:id>',views.emp_delete,name='emp_delete'),
    path('department/',views.department,name='department'),
    path('add_department',views.add_department,name='add_department'),
    path('edit_department/<int:id>',views.edit_department,name='edit_department'),
]