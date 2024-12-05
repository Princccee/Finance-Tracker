from datetime import timezone
from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'type', 'date', 'description']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount    

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['date'].initial = timezone.now().date()    

    def save(self, commit=True, user=None):
        transaction = super().save(commit=False)  # Get the instance without saving
        if user:
            transaction.user = user  # Set the user on the instance
        if commit:
            transaction.save()  # Save the instance to the database
        return transaction