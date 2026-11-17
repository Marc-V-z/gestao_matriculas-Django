from django.shortcuts import render
from .models import Aluno, Curso

# Create your views here.



def lista_alunos(request):
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'academico/alunos.html', {'alunos': alunos})


def lista_cursos(request):
    cursos = Curso.objects.prefetch_related('alunos').all()
    return render(request, 'academico/cursos.html', {'cursos': cursos})