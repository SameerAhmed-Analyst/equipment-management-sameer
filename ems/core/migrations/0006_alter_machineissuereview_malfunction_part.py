# Generated by Django 5.0.1 on 2024-04-27 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_issueclosing_delete_issueresolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineissuereview',
            name='malfunction_part',
            field=models.ManyToManyField(related_name='spares', to='core.spares'),
        ),
    ]
