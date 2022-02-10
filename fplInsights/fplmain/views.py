from django.shortcuts import render
from django.http import HttpResponse   

# Create your views here.
FPL_INSIGHTS_TEMPLATES_DIR = 'templates/fplInights'

def index(request):
    return render(request, f'{FPL_INSIGHTS_TEMPLATES_DIR}/index.html')