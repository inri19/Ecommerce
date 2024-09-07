from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Utilisateur(AbstractUser):

	adresse = models.CharField(max_length=128)
	numero_telephone = models.CharField(max_length=20)