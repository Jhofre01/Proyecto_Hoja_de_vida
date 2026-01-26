from django.contrib import admin
from .models import *
from .models import SeccionPagina


class ValidatedAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.full_clean()  # ✅ Ejecuta las validaciones del modelo
        super().save_model(request, obj, form, change)

# Registros normales o validados según el caso
admin.site.register(DatosPersonales, ValidatedAdmin)
admin.site.register(ExperienciaLaboral, ValidatedAdmin)
admin.site.register(Reconocimiento, ValidatedAdmin)
admin.site.register(CursoRealizado, ValidatedAdmin)
admin.site.register(ProductoAcademico)  # no tiene fechas
admin.site.register(ProductoLaboral, ValidatedAdmin)
admin.site.register(VentaGarage)        # no tiene fechas
admin.site.register(SeccionPagina)





