# Generated by Django 5.0.6 on 2024-06-21 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_employe', '0002_remove_paiement_employee_rename_name_departement_nom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('type_conge', models.CharField(max_length=50)),
                ('raison', models.TextField(blank=True, null=True)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_employe.employe')),
            ],
        ),
    ]