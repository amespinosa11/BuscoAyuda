from django.shortcuts import render
from .models import *
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