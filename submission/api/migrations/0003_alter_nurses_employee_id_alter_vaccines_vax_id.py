# Generated by Django 4.2.7 on 2023-11-27 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vaccines_vax_id_alter_nurses_employee_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurses',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vaccines',
            name='vax_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]