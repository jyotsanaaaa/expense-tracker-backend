from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()
    payment_method = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title