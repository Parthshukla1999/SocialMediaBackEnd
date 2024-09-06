from django.db import models
from .userModel import User
class FriendRequestModel(models.Model):
    STATUS_CHOICES = [
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Rejected'),
    ]

    sender = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)


    class Meta:
        db_table = "FriendRequest"