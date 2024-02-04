# Generated by Django 4.2.6 on 2024-01-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0038_scheme_summreportgen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summreportgen',
            name='quarter',
            field=models.CharField(choices=[('', 'All Quarters'), ('q1', 'Quarter 1 (April-June)'), ('q2', 'Quarter 2 (July-September)'), ('q3', 'Quarter 3 (October-December)'), ('q4', 'Quarter 4 (January-March)')], max_length=2),
        ),
    ]
