# Generated by Django 4.2.6 on 2024-04-19 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('matricula', models.CharField(blank=True, max_length=50, null=True)),
                ('nome_aluno', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=100)),
                ('dt_nasc', models.DateField()),
                ('endereco', models.CharField(max_length=200)),
                ('curso', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=100)),
                ('dt_nasc', models.DateField()),
                ('area_ensino', models.CharField(blank=True, max_length=100, null=True)),
                ('endereco', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Redacoes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto_redacao', models.TextField()),
                ('tema_redacao', models.CharField(max_length=200)),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRedacao.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='HistRedacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_acesso', models.DateTimeField(auto_now=True)),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRedacao.aluno')),
                ('id_redacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRedacao.redacoes')),
            ],
        ),
        migrations.CreateModel(
            name='Correcao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data_correcao', models.DateTimeField(auto_now_add=True)),
                ('id_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRedacao.professor')),
                ('id_redacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRedacao.redacoes')),
            ],
        ),
    ]
