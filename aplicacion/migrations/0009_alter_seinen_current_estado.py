# Generated by Django 4.2.4 on 2023-09-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_alter_seinen_current_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seinen',
            name='current_estado',
            field=models.CharField(choices=[('Reading', 'Reading'), ('Plan to read', 'Plan to read'), ('Completed', 'Completed')], default='Plan to read', max_length=50),
        ),
    ]
