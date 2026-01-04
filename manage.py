#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hojadevida.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # ==============================
    # CREACIÓN TEMPORAL DE SUPERUSER
    # ==============================
    try:
        import django
        django.setup()

        from django.contrib.auth.models import User

        if not User.objects.filter(username="Jhofre").exists():
            User.objects.create_superuser(
                username="Jhofre",
                email="darsa.de3@gmail.com",
                password="monserratet01"
            )
            print("✔ Superusuario creado")
    except Exception as e:
        print("Superusuario ya existe o error:", e)
    # ==============================

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

