from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved')
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
     )  
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='Pending')

    image = models.ImageField(
        upload_to='complaints/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    assigned_engineer = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='assigned_complaints'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ComplaintHistory(models.Model):
    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=20)

    updated_at = models.DateTimeField(
        auto_now_add=True
    )
    



