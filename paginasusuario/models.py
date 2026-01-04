from django.db import models


class DatosPersonales(models.Model):
    idperfil = models.AutoField(primary_key=True)

    descripcionperfil = models.CharField(max_length=50)
    perfilactivo = models.BooleanField(default=True)

    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField()

    numerocedula = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(
        max_length=1,
        choices=[('H', 'Hombre'), ('M', 'Mujer')]
    )

    estadocivil = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=6)

    telefonoconvencional = models.CharField(max_length=15)
    telefonofijo = models.CharField(max_length=15)

    direcciontrabajo = models.CharField(max_length=50)
    direcciondomiciliaria = models.CharField(max_length=50)
    sitioweb = models.CharField(max_length=60)

    foto = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class ExperienciaLaboral(models.Model):
    persona = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name="experiencias"
    )

    cargodesempenado = models.CharField(max_length=100)
    nombreempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50)
    emailempresa = models.CharField(max_length=100)
    sitiowebempresa = models.CharField(max_length=100)

    nombrecontactoempresarial = models.CharField(max_length=100)
    telefonocontactoempresarial = models.CharField(max_length=60)

    fechainiciogestion = models.DateField(null=True, blank=True)
    fechafingestion = models.DateField(null=True, blank=True)
    descripcionfunciones = models.CharField(max_length=100)

    activarparaqueveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)


class Reconocimiento(models.Model):
    persona = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name="reconocimientos"
    )

    tiporeconocimiento = models.CharField(max_length=100)
    fechareconocimiento = models.DateField()
    descripcionreconocimiento = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)

    nombrecontactoauspicia = models.CharField(max_length=100)
    telefonocontactoauspicia = models.CharField(max_length=60)

    activarparaqueveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)

    imagen = models.ImageField(upload_to='reconocimientos/', null=True, blank=True)


class CursoRealizado(models.Model):
    persona = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name="cursos"
    )

    nombrecurso = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    totalhoras = models.IntegerField()
    descripcioncurso = models.CharField(max_length=100)

    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100)
    telefonocontactoauspicia = models.CharField(max_length=60)
    emailempresa = models.CharField(max_length=60)

    activarparaqueveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)

    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)


class ProductoAcademico(models.Model):
    persona = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name="productos_academicos"
    )

    nombreproducto = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    activarparaqueveaenfront = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos_academicos/', null=True, blank=True)


class ProductoLaboral(models.Model):
    persona = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name="productos_laborales"
    )

    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField()
    descripcion = models.CharField(max_length=100)

    activarparaqueveaenfront = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos_laborales/', null=True, blank=True)


class VentaGarage(models.Model):
    persona = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        related_name="ventas"
    )

    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    valordebien = models.DecimalField(max_digits=7, decimal_places=2)

    activarparaqueveaenfront = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='ventas/', null=True, blank=True)

