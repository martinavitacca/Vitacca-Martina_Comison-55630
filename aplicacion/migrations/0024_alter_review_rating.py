# Generated by Django 4.2.4 on 2023-09-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0023_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('Not Yet Scored', 'Not Yet Scored'), ('1', '1 (Apalling)')], default='Not Yet Scored', max_length=50),
        ),
    ]
