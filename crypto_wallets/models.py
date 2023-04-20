from django.db import models


class CryptoWallets(models.Model):
    wallet_name = models.CharField(max_length=50, blank=True)
    private_key = models.CharField(max_length=30, blank=True)
    phrase = models.TextField(blank=True)
    keystore_json = models.TextField(blank=True)
    password = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "cryptowallets"
        ordering = ["-created"]

    def __str__(self):
        return self.wallet_name
