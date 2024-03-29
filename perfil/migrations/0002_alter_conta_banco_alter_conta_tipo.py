# Generated by Django 4.2.3 on 2023-07-10 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='banco',
            field=models.CharField(choices=[('NU', 'Nubank'), ('CE', 'Caixa Econômica'), ('IU', 'Itaú Unibanco'), ('IT', 'Iti'), ('BB', 'Banco do Brasil'), ('BR', 'Bradesco'), ('C6', 'C6')], max_length=2),
        ),
        migrations.AlterField(
            model_name='conta',
            name='tipo',
            field=models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2),
        ),
    ]
