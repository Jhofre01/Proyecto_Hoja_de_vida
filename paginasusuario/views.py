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
        "experiencias": persona.experiencias
            .filter(activarparaqueveaenfront=True)
            .order_by('-fechafingestion', '-fechainiciogestion'),
        "reconocimientos": persona.reconocimientos
            .filter(activarparaqueveaenfront=True)
            .order_by('-fechareconocimiento'),
        "cursos": persona.cursos
            .filter(activarparaqueveaenfront=True)
            .order_by('-fechafin', '-fechainicio'),
        "productos_academicos": persona.productos_academicos
            .filter(activarparaqueveaenfront=True)
            .order_by("nombreproducto"),
        "productos_laborales": persona.productos_laborales
            .filter(activarparaqueveaenfront=True)
            .order_by('-fechaproducto'),
        "ventas": persona.ventas
            .filter(activarparaqueveaenfront=True)
            .order_by("nombreproducto"),
    }

    return render(request, "hojadevida.html", context)


def descargar_pdf(request):
    persona = DatosPersonales.objects.first()
    config = SeccionPagina.objects.first()  # 👈 DEBE IR ARRIBA

    if not persona or not config:
        return HttpResponse("No hay datos para generar el PDF")

    secciones = request.GET.get("secciones", "")
    secciones = secciones.split(",") if secciones else []

    mostrar = []

    # Datos personales (siempre)
    if "dp" in secciones:
        mostrar.append("dp")

    if "exp" in secciones and config.mostrar_experiencia:
        mostrar.append("exp")

    if "rec" in secciones and config.mostrar_reconocimientos:
        mostrar.append("rec")

    if "cur" in secciones and config.mostrar_cursos:
        mostrar.append("cur")

    if "pa" in secciones and config.mostrar_productos_academicos:
        mostrar.append("pa")

    if "pl" in secciones and config.mostrar_productos_laborales:
        mostrar.append("pl")

    if "vg" in secciones and config.mostrar_venta_garage:
        mostrar.append("vg")

    template = get_template("hojadevida_pdf.html")

    context = {
        "persona": persona,
        "config": config,
        "mostrar": mostrar,

        "experiencias": persona.experiencias
            .filter(activarparaqueveaenfront=True)
            .order_by('-fechafingestion', '-fechainiciogestion'),

        "reconocimientos": persona.reconocimientos
            .filter(activarparaqueveaenfront=True)
            .order_by('-fechareconocimiento'),

        "cursos": persona.cursos
            .filter(activarparaqueveaenfront=True)
            .order_by('-fechafin', '-fechainicio'),

        "productos_academicos": persona.productos_academicos
            .filter(activarparaqueveaenfront=True)
            .order_by("nombreproducto"),

        "productos_laborales": persona.productos_laborales
            .filter(activarparaqueveaenfront=True)
            .order_by('-fechaproducto'),

        "ventas": persona.ventas
            .filter(activarparaqueveaenfront=True)
            .order_by("nombreproducto"),
    }

    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="hoja_de_vida.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("Error al generar el PDF")

    return response



