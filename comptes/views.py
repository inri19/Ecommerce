from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
# Create your views here.

User = get_user_model()

def SignUp(request):

	if request.method == "POST" :

		username = request.POST.get("username")
		email = request.POST.get("email")
		password = request.POST.get("password")
		adresse = request.POST.get("adresse")
		numero_telephone = request.POST.get("numero_telephone")

		if not email or not password or not adresse or not numero_telephone :

			print("Remplissez tous les champs")

		else :

			user = User.objects.create_user(username=username, email=email,adresse=adresse, numero_telephone=numero_telephone, password=password)

			#user.full_clean()

			# user.save()

			login(request, user)

			print("Utilisateur enregistrer")

			return redirect("index")

	return render(request, "comptes/inscription.html")

def logout_user(request):

	logout(request)

	return redirect("index")

def login_user(request):

	if request.method == "POST" :

		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)

		if user :
			login(request, user)

			return redirect("index")

	return render(request, 'comptes/connexion.html')