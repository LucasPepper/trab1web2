from django.shortcuts import render, get_object_or_404

from .models import Aluno, Turma

from .forms import ContatoForm

from django.contrib import messages

def AlunosListView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    queryset = Aluno.objects.all()
    context = {
        "alunos_list": queryset
    }
    return render(request, "alunos.html", context)

def AlunosDetailView(request, id): # matricula/ID_ALUNO
    obj = get_object_or_404(Turma, id=id)
    context = {
        "object": obj
    }
    return render(request, "matricula_aluno.html", context)

def contact_view(request, *args, **kwargs):
    form = ContatoForm()

    if str(request.method) == 'POST':
        print(form.is_valid())
        if form.is_valid():

            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviada')
            messages.success(request, 'E-mail enviado com sucesso')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            form = ContatoForm()

        else:

            messages.error(request,'Erro ao enviar e-mail')
            

    context = {
        'form': form
    }
    return render(request, "contact.html", context)