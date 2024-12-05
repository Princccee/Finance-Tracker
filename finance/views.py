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

# Transactions list of a particular user:
def transaction_list(request):
    transactions = Transaction.objects.filter(user = request.user)
    return render(request, 'finance/transactions.html', {'transactions': transactions})


from .forms import TransactionForm
def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)  # Pass the logged-in user to the form
            return redirect('transaction_list')  # Redirect to the transaction list page
    else:
        form = TransactionForm()  # Empty form for GET request

    return render(request, 'finance/create_transaction.html', {'form': form})


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

    return render(request, 'finance/edit_transaction.html', {'form': form})

        
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)  # Get the user's transactions
    return render(request, 'finance/transactions.html', {'transactions': transactions})        