from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from shared_app.managers import BaseManager


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    objects = BaseManager()
    original_objects = models.Manager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def undelete(self):
        self.deleted_at = None
        self.save()

    def hard_delete(self):
        return super(Base, self).delete()

    class Meta:
        abstract = True


class UserProfile(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='user/profile_pictures/', blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True, unique=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
