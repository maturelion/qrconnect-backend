from rest_framework.routers import DefaultRouter
from crypto_wallets.views import CryptoWalletViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r'crypto_wallets', CryptoWalletViewset,
                basename="crypto_wallets")

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
] + router.urls
