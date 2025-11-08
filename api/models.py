from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('workout', 'Workout'),
        ('meal', 'Meal'),
        ('steps', 'Steps'),
    ]

    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.status}"
from django.db import models

# Create your models here.
