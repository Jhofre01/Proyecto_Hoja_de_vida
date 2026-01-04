from django.shortcuts import render
from .models import DatosPersonales


def paginabienvenida(request):
    return render(request, "bienvenida.html")


def hojadevida(request):
    persona = DatosPersonales.objects.first()

    if not persona:
        return render(request, "hojadevida.html")

    context = {
        "persona": persona,
        "experiencias": persona.experiencias.filter(activarparaqueveaenfront=True),
        "reconocimientos": persona.reconocimientos.filter(activarparaqueveaenfront=True),
        "cursos": persona.cursos.filter(activarparaqueveaenfront=True),
        "productos_academicos": persona.productos_academicos.filter(activarparaqueveaenfront=True),
        "productos_laborales": persona.productos_laborales.filter(activarparaqueveaenfront=True),
        "ventas": persona.ventas.filter(activarparaqueveaenfront=True),
    }

    return render(request, "hojadevida.html", context)
