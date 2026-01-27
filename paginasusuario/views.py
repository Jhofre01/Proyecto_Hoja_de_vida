from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import DatosPersonales, SeccionPagina


def paginabienvenida(request):
    return render(request, "bienvenida.html")


def hojadevida(request):
    persona = DatosPersonales.objects.first()
    config = SeccionPagina.objects.first()  # 👈 NUEVO

    if not persona:
        return render(request, "hojadevida.html")

    context = {
        "persona": persona,
        "config": config,  # 👈 NUEVO
        "experiencias": persona.experiencias.filter(activarparaqueveaenfront=True),
        "reconocimientos": persona.reconocimientos.filter(activarparaqueveaenfront=True),
        "cursos": persona.cursos.filter(activarparaqueveaenfront=True),
        "productos_academicos": persona.productos_academicos.filter(activarparaqueveaenfront=True),
        "productos_laborales": persona.productos_laborales.filter(activarparaqueveaenfront=True),
        "ventas": persona.ventas.filter(activarparaqueveaenfront=True),
    }

    return render(request, "hojadevida.html", context)


def descargar_pdf(request):
    secciones = request.GET.get("secciones", "")
    mostrar = secciones.split(",") if secciones else []
    persona = DatosPersonales.objects.first()
    config = SeccionPagina.objects.first()  # 👈 NUEVO

    if not persona:
        return HttpResponse("No hay datos para generar el PDF")

    template = get_template("hojadevida_pdf.html")
    context = {
        "persona": persona,
        "config": config,  # 👈 NUEVO
        "experiencias": persona.experiencias.filter(activarparaqueveaenfront=True),
        "reconocimientos": persona.reconocimientos.filter(activarparaqueveaenfront=True),
        "cursos": persona.cursos.filter(activarparaqueveaenfront=True),
        "productos_academicos": persona.productos_academicos.filter(activarparaqueveaenfront=True),
        "productos_laborales": persona.productos_laborales.filter(activarparaqueveaenfront=True),
        "ventas": persona.ventas.filter(activarparaqueveaenfront=True),
        "mostrar": mostrar,
    }

    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hoja_de_vida.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("Error al generar el PDF")

    return response


