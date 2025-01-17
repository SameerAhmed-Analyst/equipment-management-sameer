# Generated by Django 5.0.1 on 2024-04-03 11:52

import django.db.models.deletion
from django.db import migrations, models


def migrate_reviews(apps, schema_editor):
    
    MachineIssue = apps.get_model('core', 'MachineIssue')
    MachineIssueReview = apps.get_model('core','MachineIssueReview')

    for issue in MachineIssue.objects.all():
        first_review = issue.machineissuereview_set.all().order_by('-reviewDate').first()
        if first_review:
            issue.temp_review_id = first_review.id
            issue.save()
            issue.machineissuereview_set.exclude(id=first_review.id).delete()




class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_reviews),
        migrations.AddField(
            model_name='machineissue',
            name='temp_review_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='machineissuereview',
            name='issue',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.machineissue'),
        ),
    ]
