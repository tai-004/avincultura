# Generated by Django 4.0.8 on 2023-07-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_relacao_text_remove_relacao_fixos_relacao_fixos'),
    ]

    operations = [
        migrations.AddField(
            model_name='diario',
            name='fixos',
            field=models.ManyToManyField(to='app1.fixos'),
        ),
    ]