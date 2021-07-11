from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    balance=models.FloatField()

class transaction_history(models.Model):
    timestamp = models.DateTimeField(auto_now=True,null=True)
    sender = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='receiver')
    amount = models.FloatField()

