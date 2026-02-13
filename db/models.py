from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)  # Pode ser vazio (blank)


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    # Se a Race for deletada, a Skill também é (CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)  # O requisito diz especificamente "pode ser null"


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)  # EmailField é melhor, mas CharField aceita também
    bio = models.CharField(max_length=255)

    # Se Race for deletada, Player é deletado
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    # Se Guild for deletada, Player NÃO é deletado (SET_NULL).
    # null=True é obrigatório aqui para permitir que o campo fique vazio.
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)