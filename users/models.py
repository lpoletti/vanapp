from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = 'ADMIN', 'Admin'
#         STUDENT = 'STUDENT', 'Estudante'
#         TEACHER = 'TEACHER', "Professor(a)"
#         RIDER = 'RIDER', 'Motorista'
#         RESPONSIBLE = 'RESPONSIBLE', 'Responsável'
#         MONITOR = 'MONITOR', 'Monitor(a)'

#     uuid = models.UUIDField(primary_key=True,default=uuid4, editable=False)
#     firs_name = models.CharField(max_length=50)