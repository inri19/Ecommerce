from django.shortcuts import render, get_object_or_404, redirect
from boutique.models import Produit, Commande, Panier, Categorie
from django.urls import reverse
# EMAIL LIB

from .email_sender import envoyer_email
from email.message import EmailMessage
import ssl 
import smtplib


# Create your views here.
def index(request):

	produits = Produit.objects.all()
	categories = Categorie.objects.all()

	return render(request, "boutique/index.html", context={ "produits" : produits, "categories" : categories })


def detail_produit(request, slug):

	produit = get_object_or_404(Produit, slug = slug)

	return render(request, "boutique/produit_detail.html", context = {"produit" : produit})
 
def add_to_cart(request, slug):

	user = request.user
	produit = get_object_or_404(Produit, slug=slug)

	panier, _ = Panier.objects.get_or_create(user=user)
	commande, creer = Commande.objects.get_or_create(user=user, produit=produit, commande_valider=False)

	if creer:

		panier.commandes.add(commande)
		panier.save()

	else :

		commande.quantite += 1
		commande.save()

	return redirect("index")

def panier(request): 

	user = request.user
	panier = get_object_or_404(Panier, user=request.user)

	total = 0.0
	commandes_user = ""

	# panier.commandes.all().annotate(tot=commande.produit.prix * commande.quantite)

	for commande in panier.commandes.all() :

		total += commande.produit.prix * commande.quantite
		cmd = str(commande.produit.nom) + " " + str(commande.quantite) + "\n"
		commandes_user +=  cmd
	
	if request.method == "POST" :

		valide_commande = request.POST.get("valider_commande")

		if valide_commande == "good" :

			text = f"Email : {user.email} \nNumero Telephone : {user.numero_telephone} \n Adresse : {user.adresse}\n"
			text += commandes_user

			try :
				envoyer_email(email_send="doxaranjm@gmail.com", subject="Commande", content=text)
				print("Email bien envoyer ")

				return redirect("commande_valider")
			except Exception as e :
				print(type(e))
				print(e.args)
				print(e)
	

	return render(request, "boutique/panier.html", context = {"panier" : panier.commandes.all(), "montant_tot" : total})

def panier_delete(request):

	panier = request.user.panier

	if panier :
		panier.commandes.all().delete()

	return redirect("index")

def commande_valider(request):

	user = request.user

	if not user :

		return redirect("index")

	panier = request.user.panier

	if panier :
		panier.commandes.all().delete()

	return render(request, "boutique/commande_valider.html", context = {})

def produits_par_categorie(request, slug_cat):

	categorie = get_object_or_404(Categorie, nom=slug_cat)
	produits = Produit.objects.filter(categorie=categorie)

	return render(request, "boutique/categorie.html", context = { "categorie" : categorie, "produits" : produits })
