from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from RestaurantManagement.models import Restaurant

class User(AbstractUser):
    ROLE_CHOICES = (
        ('administrator', 'Administrator'),
        ('restaurant_owner', 'Restaurant Owner'),
        ('restaurant_staff', 'Restaurant Staff'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    groups = models.ManyToManyField(Group, related_name='user_management_users')
    user_permissions = models.ManyToManyField(Permission, related_name='user_management_users_permissions')
    restaurants = models.ManyToManyField(Restaurant, related_name='staff_members')
    birthdate = models.DateField(default="2000-01-01")
