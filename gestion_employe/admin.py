from django.contrib import admin
from .models import Departement, Employe, Paiement, Conge

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'telephone', 'departement', 'date_embauche')
    search_fields = ('prenom', 'nom', 'email')
    list_filter = ('departement', 'date_embauche')

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('employe', 'montant', 'date_paiement', 'type_paiement')
    search_fields = ('employe__prenom', 'employe__nom', 'type_paiement')
    list_filter = ('date_paiement', 'type_paiement')

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date_debut', 'date_fin', 'type_conge', 'raison')
    search_fields = ('employe__prenom', 'employe__nom', 'type_conge')
    list_filter = ('date_debut', 'date_fin', 'type_conge')