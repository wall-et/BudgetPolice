from django.db import models

class Expense(models.Model):
    date = models.DateField('date published')
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}, cost {self.amount} on {self.date}."
