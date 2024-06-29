# Generated by Django 5.0.6 on 2024-06-21 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_employe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paiement',
            name='employee',
        ),
        migrations.RenameField(
            model_name='departement',
            old_name='name',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='paiement',
            old_name='payment_date',
            new_name='date_paiement',
        ),
        migrations.RenameField(
            model_name='paiement',
            old_name='amount',
            new_name='montant',
        ),
        migrations.RenameField(
            model_name='paiement',
            old_name='payment_type',
            new_name='type_paiement',
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('date_embauche', models.DateField()),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_employe.departement')),
            ],
        ),
        migrations.AddField(
            model_name='paiement',
            name='employe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_employe.employe'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]