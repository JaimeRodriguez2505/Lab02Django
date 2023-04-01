from django.shortcuts import render

# Create your views here.


def formulario(request):
    return render(request, 'calcularc/formulario.html')


def calcular(request):
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        radio = diametro / 2
        volumen = 3.1416 * radio ** 2 * altura
        return render(request, 'calcularc/resultado.html', {'cilindro': volumen})
    else:
        return render(request, 'calcularc/formulario.html')