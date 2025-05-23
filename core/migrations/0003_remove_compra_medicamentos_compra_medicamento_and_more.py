# Generated by Django 5.2.1 on 2025-05-13 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_medicamento_preco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='medicamentos',
        ),
        migrations.AddField(
            model_name='compra',
            name='medicamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='core.medicamento'),
        ),
        migrations.AddField(
            model_name='compra',
            name='quantidade',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='compra',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]
