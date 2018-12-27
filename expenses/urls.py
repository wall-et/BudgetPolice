from django.urls import path

from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    # path('lucky', views.lucky, name='lucky'),
    # path('multi-table', views.multi_table, name='multi_table'),
]