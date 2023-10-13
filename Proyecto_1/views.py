from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Formulario(request):

    return render(request, "Formulario.html")

@csrf_exempt
def notas_formulario(request):

    nombre1 = str (request.POST["Nombre"])
    rut1 = str (request.POST["Rut"])
    modulo1 = str (request.POST["Modulo"])

    nota1 = float (request.POST["Nota_1"])
    nota2 = float (request.POST["Nota_2"])
    nota3 = float (request.POST["Nota_3"])
    nota4 = float (request.POST["Nota_4"])
    nota5 = float (request.POST["Nota_5"])
    nota6 = float (request.POST["Nota_6"])
    
    promedio_final = round((nota1*0.15)+(nota2*0.15)+(nota3*0.2)+(nota4*0.2)+(nota5*0.15)+(nota6*0.15), 1)

    return render(request, "promedios.html", {"nombre1": nombre1, "rut1": rut1, "modulo1": modulo1, "nota1": nota1, "nota2": nota2, "nota3": nota3, "nota4": nota4, "nota5": nota5, "nota6": nota6, "promedio_final": promedio_final})


