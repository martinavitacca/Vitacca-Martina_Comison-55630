# Generated by Django 4.2.4 on 2023-09-02 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_addentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addentry',
            options={'ordering': ['title'], 'verbose_name': 'AddEntry', 'verbose_name_plural': 'AddEntries'},
        ),
    ]
