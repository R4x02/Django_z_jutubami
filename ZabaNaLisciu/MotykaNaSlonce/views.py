from django.shortcuts import render
from .models import ZDeszczuPodRynne
# Create your views here.
def glowica(atomowa):
    DATUS_Z_MODELUSA = ZDeszczuPodRynne.objects.all()
    return render(atomowa, template_name='index.html', context={"DO_ALMTH" : DATUS_Z_MODELUSA})