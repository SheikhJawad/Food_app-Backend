# api/models.py
from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    reservation_date = models.DateTimeField()
    people_count = models.IntegerField()
    special_request = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.reservation_date}"
