# Generated by Django 3.2.7 on 2023-04-20 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_wallets', '0002_auto_20220310_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cryptowallets',
            options={'ordering': ['-created'], 'verbose_name_plural': 'cryptowallets'},
        ),
    ]