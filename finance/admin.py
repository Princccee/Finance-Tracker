from django.contrib import admin
from .models import Transaction, Budget, SavingsGoal

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'category', 'type', 'date')
    list_filter = ('type', 'date')
    search_fields = ('category', 'description')

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'start_date', 'end_date')
    list_filter = ('category',)

@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'target_amount', 'current_amount', 'deadline')
    search_fields = ('name',)