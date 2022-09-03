from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
    CHOICES_ESCOLARIDADE = [
        ("IN", "Ensino Infantil"),
        ("ME", "Ensino Médio"),
        ("SU", "Ensino Superior"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    escolaridade = models.CharField(
        max_length=255,
        choices=CHOICES_ESCOLARIDADE,
    )

    data_nascimento = models.DateField(null=True, blank=True)
