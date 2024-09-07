from django.db import models
from shop.settings import AUTH_USER_MODEL

# Create your models here.
"""

Produit 
- Nom
- Prix
- Quantite en stock
- Description
- Image


"""
class Categorie(models.Model):

	nom = models.CharField(max_length=128)

	def __str__(self):
		return self.nom

class Produit(models.Model):

	nom = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128)
	prix = models.FloatField(default=0.0)
	quantite = models.IntegerField(default=0)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to="produits", blank=True, null=True)
	categorie = models.ForeignKey(Categorie, related_name="categorie", on_delete=models.CASCADE)

	def __str__(self):
		return self.nom

class Commande(models.Model):

	user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
	produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
	quantite = models.IntegerField(default=1)
	commande_valider = models.BooleanField(default=False)
	date_commande = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f"{self.produit.nom} ({self.quantite})"


class Panier(models.Model):

	user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
	commandes = models.ManyToManyField(Commande)

	def __str__(self):
		return self.user.username