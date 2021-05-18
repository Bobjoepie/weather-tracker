"""
Definition of models.
"""

from django.db import models

# Create your models here.

Descriptions = (
    (0, "Sunny"),
    (1, "Rain"),
    (2, "Cloudy"),
    (4, "Snow")
    )

class Description(models.Model):
    """Model to describe the weather"""
    description = models.IntegerField(choices=Descriptions, default=0)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']