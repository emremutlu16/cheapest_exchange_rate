from django.db import models

# Create your models here.


class ProviderValues(models.Model):
    provider_name = models.CharField(max_length=50, null=False, blank=False)
    usd = models.FloatField(null=False, blank=False)
    eur = models.FloatField(null=False, blank=False)
    gbp = models.FloatField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=True)
