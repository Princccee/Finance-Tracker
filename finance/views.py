from django.shortcuts import render, redirect
from .models import Transaction, Budget, SavingsGoal
# Create your views here.

def user_transactions(request):
    transactions = Transaction.objects.filter(user =  request.user)
    return transactions

def user_budget(request):
    budgets = Budget.objects.filter(user = request.user)
    return budgets


def user_goals(request):
    goals = SavingsGoal.objects.filter(user = request.user)
    return goals


#----------------------------------------------------------------------------------------------
# Transactions list of a particular user:
def transaction_list(request):
    transactions = Transaction.objects.filter(user = request.user)
    return render(request, 'finance/transactions.html', {'transactions': transactions})

# Create transaction for user:
from .forms import TransactionForm 
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)  # Pass the logged-in user to the form
            return redirect('transaction_list')  # Redirect to the transaction list page
    else:
        form = TransactionForm()  # Empty form for GET request

    return render(request, 'transactions/create_transaction.html', {'form': form})


# Edit transactions:
from django.shortcuts import get_object_or_404

def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)  # Ensure it belongs to the user
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save(user=request.user)  # Pass the user to the form
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)  # Pre-fill with the existing data

    return render(request, 'transactions/edit_transaction.html', {'form': form})

# Get the transaction list of user        
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)  # Get the user's transactions
    return render(request, 'transactions/transactions.html', {'transactions': transactions})       

#----------------------------------------------------------------------------------------------
# View to handle setting a budget
from .forms import BudgetForm
def set_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user  # Associate budget with the logged-in user
            budget.save()
            return redirect('budget_list')  # Redirect to a budget list page
    else:
        form = BudgetForm()
    return render(request, 'budgets/set_budget.html', {'form': form})

#----------------------------------------------------------------------------------------------
# Dasboard
from django.db.models import Sum

def dashboard(request):
    # Aggregate data for dashboard
    total_income = Transaction.objects.filter(type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = Transaction.objects.filter(type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
    
    monthly_data = (
        Transaction.objects.values('date__month')
        .annotate(total_amount=Sum('amount'))
        .order_by('date__month')
    )
    months = [entry['date__month'] for entry in monthly_data]
    monthly_totals = [entry['total_amount'] for entry in monthly_data]

    category_data = (
        Transaction.objects.filter(type='Expense')
        .values('category')
        .annotate(total_amount=Sum('amount'))
        .order_by('-total_amount')
    )
    categories = [entry['category'] for entry in category_data]
    category_totals = [entry['total_amount'] for entry in category_data]

    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'months': months,
        'monthly_totals': monthly_totals,
        'categories': categories,
        'category_totals': category_totals,
    }
    return render(request, 'dashboard/dashboard.html', context)