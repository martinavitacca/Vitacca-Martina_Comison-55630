# Generated by Django 4.2.4 on 2023-09-02 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0020_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('comment', models.TextField(null=True)),
                ('rating', models.CharField(choices=[(0, 'Not Yet Scored'), (1, 'Apalling'), (2, 'Horrible'), (3, 'Very Bad'), (4, 'Bad'), (5, 'Avarage'), (6, 'Fine'), (7, 'Good'), (8, 'Very Good'), (9, 'Great'), (10, 'Masterpiece')], default=0, max_length=50)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ['username'],
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
