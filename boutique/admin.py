from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Panier)
admin.site.register(Categorie)