# Generated by Django 4.2.4 on 2023-09-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0013_rename_japanese_title_manhwa_korean_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('chapter', models.IntegerField(default=0)),
                ('volume', models.IntegerField(default=0)),
                ('current_estado', models.CharField(choices=[('Reading', 'Reading'), ('Plan to read', 'Plan to read'), ('Completed', 'Completed')], default='Plan to read', max_length=50)),
            ],
        ),
    ]
