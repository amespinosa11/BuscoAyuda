from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
	return render(request, "index.html")


def registro(request):
	form = TrabajadorForm
	user_form = UserForm
	context = {
        'form': form,
        'user_form': user_form
    }
	return render(request, "registro.html", context)