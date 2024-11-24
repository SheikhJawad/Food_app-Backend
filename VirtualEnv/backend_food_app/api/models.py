from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    reservation_date = models.DateTimeField()
    people_count = models.IntegerField()
    special_request = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.reservation_date}"


class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=True)  # True = Active, False = Inactive
    created_at = models.DateTimeField(default=timezone.now)
    
    def deactivate_user(self):
        """Deactivates the user and deletes the access token"""
        self.status = False
        self.save()
        self.delete_access_token()  
    
    def delete_access_token(self):
        """Delete access token when inactive"""
        self.access_token = None
        self.save()

    def delete_refresh_token(self):
        """Delete refresh token if needed"""
        self.refresh_token = None
        self.save()
    
    def __str__(self):
        return f"Token for {self.user.username} - Active: {self.status}"

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name
