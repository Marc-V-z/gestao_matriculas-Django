from django.db import models

# Create your models here.


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField()

    def __str__(self):
        return self.titulo


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    cursos = models.ManyToManyField(Curso, blank=True, related_name='alunos')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'