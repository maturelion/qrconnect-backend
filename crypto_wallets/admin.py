from django.contrib import admin
from .models import CryptoWallets


class WalletNameAdmin(admin.ModelAdmin):
    list_display = ['wallet_name']


admin.site.register(CryptoWallets, WalletNameAdmin)
