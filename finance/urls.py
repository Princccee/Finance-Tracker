from django.urls import path
from . import views

urlpatterns = [
    path('transactions_list/', views.transaction_list, name='transaction_list'),
    path('user_transactions/', views.user_transactions, name='user_transactions'),
    path('user_budget/', views.user_budget, name='user_budget'),
    path('user_goals/', views.user_goals, name='user_goals'),
    path('transactions/create/', views.create_transaction, name='create_transactions'),
    path('budgets/set_budget/', views.set_budget, name="set_budget"),
]