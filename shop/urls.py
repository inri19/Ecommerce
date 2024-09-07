"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from boutique.views import index, detail_produit, add_to_cart, panier, panier_delete
from comptes.views import SignUp, logout_user, login_user
from shop import settings

urlpatterns = [
	path('', index, name="index"),
	path('produit/<str:slug>/', detail_produit, name="detail_produit"),
    path('produit/<str:slug>/add_to_cart/', add_to_cart, name="add_to_cart"),
    path('panier/', panier, name="panier"),
    path('panier/supprimer/', panier_delete, name="panier_delete"),
	path('inscription/', SignUp, name="SignUp"),
    path('connexion/', login_user, name="login_user"),
    path('deconnexion/', logout_user, name="logout"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
