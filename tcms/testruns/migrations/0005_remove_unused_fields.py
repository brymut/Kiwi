# Generated by Django 2.1.5 on 2019-01-19 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testruns', '0004_squashed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaltestcaserun',
            old_name='case_run_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='testcaserun',
            old_name='case_run_status',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='historicaltestcaserun',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='historicaltestcaserun',
            name='running_date',
        ),
        migrations.RemoveField(
            model_name='testcaserun',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='testcaserun',
            name='running_date',
        ),
    ]