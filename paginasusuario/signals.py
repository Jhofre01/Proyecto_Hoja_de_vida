from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_migrate)
def crear_superusuario(sender, **kwargs):
    username = "Jhofre"
    email = "darsa.de3@gmail.com"
    password = "monserratet01"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("✔ Superusuario creado automáticamente")
