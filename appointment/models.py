from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=155)
    comments = models.TextField()
    in_process = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    time_added = models.TimeField(auto_now_add=True)

    
    def __str__(self):
        return self.first_name + " | " + self.email