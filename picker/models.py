from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Plan(models.Model):
    """
    Model representing a Plan
    """
    # Fields

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, help_text='Enter a brief description')

    PRICE_RANGE = (
        ('$', 'Cheap'),
        ('$$', 'Moderate'),
        ('$$$', 'Pricey'),
    )

    price_point = models.CharField(max_length=3, choices=PRICE_RANGE, blank=True, help_text='Price Range')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)

    # Methods

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Plan
        """
        return reverse('plan-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing a Plan object
        """
        return self.title
    
class Location(models.Model):
    """
    Model representing a location
    """

    # Fields 
    name = models.CharField(max_length=200)


    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Location
        """
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class PlanManager(models.Model):
    """
    Model to get a random plan
    """
    # Methods
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count-1)
        return self.all()[random_index]