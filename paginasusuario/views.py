from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
import tempfile

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


def descargar_pdf(request):
    persona = DatosPersonales.objects.first()

    if not persona:
        return HttpResponse("No hay datos registrados", status=404)

    context = {
        "persona": persona,
        "experiencias": persona.experiencias.filter(activarparaqueveaenfront=True),
        "reconocimientos": persona.reconocimientos.filter(activarparaqueveaenfront=True),
        "cursos": persona.cursos.filter(activarparaqueveaenfront=True),
        "productos_academicos": persona.productos_academicos.filter(activarparaqueveaenfront=True),
        "productos_laborales": persona.productos_laborales.filter(activarparaqueveaenfront=True),
        "ventas": persona.ventas.filter(activarparaqueveaenfront=True),
    }

    template = get_template("hojadevida.html")
    html = template.render(context)

    with tempfile.NamedTemporaryFile(delete=True) as output:
        HTML(string=html).write_pdf(output.name)
        output.seek(0)

        response = HttpResponse(
            output.read(),
            content_type="application/pdf"
        )
        response["Content-Disposition"] = 'attachment; filename="Hoja_de_Vida.pdf"'
        return response

