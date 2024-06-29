from django.db import models

class Departement(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Employe(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    date_embauche = models.DateField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Paiement(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE,blank=True, null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()
    type_paiement = models.CharField(max_length=50)  # e.g., "Salaire", "Prime", etc.

    def __str__(self):
        return f"{self.employe} - {self.montant} le {self.date_paiement}"

class Conge(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    type_conge = models.CharField(max_length=50)  # e.g., "Vacances", "Maladie", etc.
    raison = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employe} - {self.type_conge} du {self.date_debut} au {self.date_fin}"