# Generated by Django 4.2.6 on 2024-01-22 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0031_alter_proposal_approved_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='total_duration',
            new_name='component_wise_duration',
        ),
    ]