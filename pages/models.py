from django.db import models

# https://stackoverflow.com/questions/31130706/dropdown-in-django-model
SITUACAO_ALUNO_CHOICES = (
    ('Aprovado', 'APROVADO'),
    ('Reprovado', 'REPROVADO'),
    ('Matriculado', 'MATRICULADO'),
    ('Dispensado', 'DISPENSADO'),
    ('Cancelado', 'CANCELADO'),
)

SITUACAO_TURMA_CHOICES = (
    ('Aberta', 'ABERTA'),
    ('Fechada', 'FECHADA'),
    ('Cancelada', 'CANCELADA'),
)

CURSO_CHOICES = (
    ('bsi', 'BSI'),
    ('tads', 'TADS'),
)

PERIODO_CHOICES = (
    ('2023/1', '2023/1'),
    ('2022/2', '2022/2'),
    ('2022/1', '2022/1'),
    ('2021/2', '2021/2'),
    ('2021/1', '2022/1'),
    ('2020/2', '2020/2'),
    ('2020/1', '2020/2'),
    ('2019/2', '2019/2'),
    ('2019/1', '2019/1'),
    ('2018/2', '2018/2'),
    ('2018/1', '2018/1'),
)

class Aluno(models.Model):
    # PK = ID = Nº Matrícula
    pk_aluno = 1
    nome = models.CharField('Nome', max_length=100)
    periodoIngresso = models.CharField('Período de Ingresso', max_length=15, choices=PERIODO_CHOICES)
    foto = models.ImageField(upload_to='images/')
    cpf = models.CharField('CPF', max_length=11) # Somente números
    rg = models.CharField('RG', max_length=8) # Somente números 
    curso = models.CharField('Curso', max_length=15, choices=CURSO_CHOICES)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    disciplina = models.CharField(max_length=20)

    def __str__(self):
        return self.disciplina
    
class Turma(models.Model):
    aluno = models.ManyToManyField(Aluno, related_name="turmas") # FK_ALUNO (Nº Matrícula)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, blank=True, null=True, default=1) # FK_ALUNO (Nº Matrícula)
    nome = disciplina.get_attname
    periodo = models.CharField(choices=PERIODO_CHOICES, max_length=15) # PK
    data_abertura = models.DateField('Data')

    def __str__(self):
        return f'{self.disciplina} {self.periodo} '
    
class TurmaAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT) # FK_ALUNO (Nº Matrícula)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT) # FK_TURMA (Cód_Turma)
    nota = models.DecimalField('Nota', decimal_places=1, max_digits=3) # Cada aluno possui uma nota NAQUELA Turma
    situacao_aluno = models.CharField('Situação do Aluno', max_length=15, choices=SITUACAO_ALUNO_CHOICES) # Cada aluno possui uma situação NAQUELA Turma

    def __str__(self):
        return f'{self.aluno} {self.turma} {self.nota} {self.situacao_aluno}  '

# class Turma_Disciplina(models.Model):
#     aluno = models.ForeignKey(to=Aluno, on_delete=) # FK_ALUNO (Nº Matrícula)
#     turma = models.ForeignKey(to=Turma, on_delete=) # FK_TURMA (Cód_Turma)
#     nota = models.DecimalField('Nota', decimal_places=1, max_digits=3) # Cada aluno possui uma nota NAQUELA Turma
#     situacao_aluno = models.CharField('Situação do Aluno', max_length=15, choices=SITUACAO_ALUNO_CHOICES) # Cada aluno possui uma situação NAQUELA Turma
    
class Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=50)
    texto = models.CharField(max_length=120)