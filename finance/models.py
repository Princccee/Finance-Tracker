from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Transaction Model
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    CATEGORY = [
        ('education', 'Education'),
        ('rent', 'Rent'),
        ('food', 'Food'),
        ('groceries', 'Groceries'),
        ('health', 'Health'),
        ('maintainance', 'Maintainance'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to a user
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Up to 10 digits with 2 decimals
    category = models.CharField(max_length=50, choices=CATEGORY) # Category of transactions( rent, groceries, health, foof, education, ......)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    date = models.DateField() #The date of the transaction
    description = models.TextField(blank=True, null=True) # A short description of the transaction.

    # dunder method: It is used to return a human-readable string representation of an object.
    def __str__(self):
        return f"{self.type.capitalize()} - {self.category} - {self.amount}"


# Budget Model
class Budget(models.Model):
    CATEGORY = [
        ('education', 'Education'),
        ('rent', 'Rent'),
        ('food', 'Food'),
        ('groceries', 'Groceries'),
        ('health', 'Health'),
        ('maintainance', 'Maintainance'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to a user
    category = models.CharField(max_length=50, choices= CATEGORY)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    
    # Dunder method:
    def __str__(self):
        return f"Budget for {self.category} - {self.amount}"
    
    # Prevent Budgets Without an Associated User
    def clean(self):
        if not self.user:
            raise ValidationError("Each budget must be associated with a user.")


# Savings Goal Model
class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to a user
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    deadline = models.DateField()

    def __str__(self):
        return f"{self.name} - Target: {self.target_amount}"