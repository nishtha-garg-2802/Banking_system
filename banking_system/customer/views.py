
from django.shortcuts import render,redirect
from .models import transaction_history,customer
import re
from django.contrib import messages
all_customer=customer.objects.all()

# Create your views here.
def home(request):
    return render(request,'customer/index.html')

def customer_list(request):
    all_customer=customer.objects.all().order_by('id')
    return render(request,'customer/customer.html',{'customer_list':all_customer})

def history(request):
    all_history=transaction_history.objects.all().order_by('id')
    return render(request,'customer/history.html',{'transfer_his':all_history})

def profile(request,cust_id):
    sender=customer.objects.get(id=cust_id)
    if request.method=='POST':
        receiver_id=request.POST['receiver']
        if request.POST['amount_transfer']=='' or not re.match('[+-]?([0-9]*[.])?[0-9]+',request.POST['amount_transfer']):
            messages.error(request,'Please enter valid amount to transfer')
        else:
            amount=float(request.POST['amount_transfer'])
        
        if receiver_id == 'Select Customer':
            messages.error(request,'Please select a customer')
        else:
            receiver=customer.objects.get(id=receiver_id)
            if not amount>sender.balance:
                sender.balance=(sender.balance-amount)
                receiver.balance=(receiver.balance+amount)
                sender.save()
                receiver.save()
                transfer_money=transaction_history(sender=sender,receiver=receiver,amount=amount)
                transfer_money.save()
                messages.success(request,'Amount is transferred successfully!!')
            else:
                messages.error(request,'Insufficient balance')
    
    return render(request,'customer/profile.html',{'customer_list':all_customer,'sender':sender})


def messages_pg(request):
    return render(request,'message.html')