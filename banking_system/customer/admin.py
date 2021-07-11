from django.contrib import admin
from .models import customer,transaction_history

# Register your models here.

admin.site.register(customer)
admin.site.register(transaction_history)
