from django.db import models
from .userModel import User
from django.contrib.postgres.fields import ArrayField

class FriendsModel(models.Model):
    user = models.ForeignKey(User, related_name='friendship', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)


    class Meta:
        db_table = "Friends"