from django.shortcuts import render, get_object_or_404

from .models import Aluno, Turma

def AlunosListView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    queryset = Aluno.objects.all()
    context = {
        "aluno_list": queryset
    }
    return render(request, "alunos.html", context)

def AlunosDetailView(request, id): # matricula/ID_ALUNO
    obj = get_object_or_404(Turma, id=id)
    context = {
        "object": obj
    }
    return render(request, "matricula_aluno.html", context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})