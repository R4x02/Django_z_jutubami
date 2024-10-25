from django.db import models

# Create your models here.
class DobrzeZObcymGdySieDobrzeZna(models.Model):
    pole_gdzie_te_po_przecinku_sa = models.FloatField()

class ZDeszczuPodRynne(models.Model):
    literkowe_pole = models.CharField(max_length= 100)
    numerkowe_pole = models.IntegerField()
    pole_klucza_nie_z_tej_ziemi = models.ForeignKey(DobrzeZObcymGdySieDobrzeZna, on_delete=models.CASCADE)