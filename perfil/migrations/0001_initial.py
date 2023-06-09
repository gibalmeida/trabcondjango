# Generated by Django 4.1.3 on 2023-03-20 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_de_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pessoa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_instituicao', models.CharField(max_length=200)),
                ('data_de_inicio', models.DateField()),
                ('date_de_termino', models.DateField(null=True)),
                ('situacao_atual_do_curso', models.CharField(choices=[('A', 'Em Andamento'), ('I', 'Interrompido/Desistiu'), ('S', 'Suspenso/Trancado'), ('C', 'Concluído')], default='C', max_length=1)),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.pessoa')),
            ],
            options={
                'verbose_name': 'Formação',
                'verbose_name_plural': 'Formações',
            },
        ),
        migrations.CreateModel(
            name='Emprego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_organizacao', models.CharField(max_length=200)),
                ('data_de_inicio', models.DateField()),
                ('data_de_termino', models.DateField(null=True)),
                ('descricao_das_principais_atividades', models.TextField()),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfil.pessoa')),
            ],
            options={
                'verbose_name_plural': 'Empregos',
            },
        ),
    ]
