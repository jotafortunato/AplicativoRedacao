# Generated by Django 4.2.6 on 2024-04-19 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appRedacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'verbose_name_plural': 'Alunos'},
        ),
        migrations.AlterModelOptions(
            name='correcao',
            options={'verbose_name_plural': 'Correcoes'},
        ),
        migrations.AlterModelOptions(
            name='histredacao',
            options={'verbose_name_plural': 'HistRedacoes'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name_plural': 'Professores'},
        ),
        migrations.AlterModelOptions(
            name='redacoes',
            options={'verbose_name_plural': 'Redacoes'},
        ),
    ]