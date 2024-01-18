# Generated by Django 4.2.6 on 2024-01-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0027_rename_training_details_wtc_sheet_wooltestinglab_training_details_wdtc_sheet_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domesticmeeting',
            old_name='master_trainer_details_sheet',
            new_name='participants_details_sheet',
        ),
        migrations.RenameField(
            model_name='organisingseminar',
            old_name='master_trainer_details_sheet',
            new_name='participants_details_sheet',
        ),
        migrations.RenameField(
            model_name='wooltestinglab',
            old_name='training_details_wdtc_sheet',
            new_name='training_details_wtc_sheet',
        ),
        migrations.RemoveField(
            model_name='domesticmeeting',
            name='office_assistant_details_sheet',
        ),
        migrations.RemoveField(
            model_name='domesticmeeting',
            name='payment_proofs',
        ),
        migrations.RemoveField(
            model_name='domesticmeeting',
            name='topics_covered_sheet',
        ),
        migrations.RemoveField(
            model_name='domesticmeeting',
            name='trainee_details_sheet',
        ),
        migrations.RemoveField(
            model_name='organisingseminar',
            name='office_assistant_details_sheet',
        ),
        migrations.RemoveField(
            model_name='organisingseminar',
            name='topics_covered_sheet',
        ),
        migrations.RemoveField(
            model_name='organisingseminar',
            name='trainee_details_sheet',
        ),
        migrations.RemoveField(
            model_name='publicitymonitoring',
            name='duration_from',
        ),
        migrations.RemoveField(
            model_name='publicitymonitoring',
            name='duration_to',
        ),
        migrations.RemoveField(
            model_name='publicitymonitoring',
            name='training_details',
        ),
        migrations.RemoveField(
            model_name='wpssmalltoolsdistribution',
            name='total_equipment_shared',
        ),
        migrations.AddField(
            model_name='proposal',
            name='fund_allocated',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='proposal',
            name='sanction_letter',
            field=models.FileField(null=True, upload_to='sanction_letters/'),
        ),
        migrations.AddField(
            model_name='wms_buyersellerexpo',
            name='quarterly_allocated_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='wms_infrastructuredevelopment',
            name='quarterly_allocated_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.DeleteModel(
            name='SanctionLetter',
        ),
    ]