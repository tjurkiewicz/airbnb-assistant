import django.contrib.auth.models
import django.db.models


class AirBNBAuthInfo(django.db.models.Model):
    user = django.db.models.OneToOneField(
        django.contrib.auth.models.User,
        on_delete=django.db.models.CASCADE)

    access_token = django.db.models.CharField(max_length=32)
    raw = django.db.models.TextField()