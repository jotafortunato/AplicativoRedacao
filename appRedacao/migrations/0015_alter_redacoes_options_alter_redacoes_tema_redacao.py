# Generated by Django 5.0.2 on 2024-06-06 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appRedacao', '0014_alter_temaredacao_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='redacoes',
            options={},
        ),
        migrations.AlterField(
            model_name='redacoes',
            name='tema_redacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appRedacao.temaredacao'),
        ),
    ]
