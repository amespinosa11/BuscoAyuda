from django.shortcuts import render, redirect
from .models import *
from django.contrib import auth
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def index(request):
	trabajadores = Trabajador.objects.all()
	context = {
		'trabajadores':trabajadores
	}
	return render(request, "index.html", context)


def registro(request):
	form = TrabajadorForm
	user_form = UserForm
	user = request.user
	#Trabajador.objects.first().nombre
	context = {
        'form': form,
        'user_form': user_form,
        'user': user
    }
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = User.objects.create_user(username=username, password=password)
		user.first_name = request.POST.get('nombre')
		user.last_name = request.POST.get('apellidos')
		user.email = request.POST.get('correo')
		user.save()


		nuevo_trabajador=Trabajador(nombre=request.POST['nombre'],
                                      apellidos=request.POST['apellidos'],
                                      aniosExperiencia=request.POST.get('aniosExperiencia'),
                                      tiposDeServicio=TiposDeServicio.objects.get(pk=request.POST.get('tiposDeServicio')),
                                      telefono=request.POST.get('telefono'),
                                      correo=request.POST.get('correo'),
                                      #imagen=request.FILES['imagen'],
                                      usuarioId=user)
		nuevo_trabajador.save()
		#return HttpResponseRedirect('/')

	return render(request, "registro.html", context)


def detalle(request, id):
	detalles_trabajador = Trabajador.objects.get(id = id)
	context = {
		'detalles_trabajador':detalles_trabajador
	}
	return render(request, "detalle.html", context)

def login(request):
	user_form = UserForm
	context = {
		'user_form': user_form
	}

	if request.method == 'POST':
	    username = request.POST.get('username')
	    password = request.POST.get('password')
	    user = auth.authenticate(username=username, password=password)
	    if user is not None:
	        auth.login(request, user)
	        messages.success(request, "Bienvenido al sistema {}".format(username), extra_tags="alert-success")
	        return redirect(reverse('index'))
	    else:
	        messages.error(request, "¡El usuario o la contraseña son incorrectos!", extra_tags="alert-danger")
	        return redirect(reverse('index'))

	return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    messages.info(request, "Cerraste sesión exitosamente", extra_tags="alert-info")
    return redirect(reverse('index'))