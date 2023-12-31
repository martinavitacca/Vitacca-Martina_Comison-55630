# Generated by Django 4.2.4 on 2023-09-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_alter_seinen_current_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('title_recommendation', models.CharField(max_length=100)),
                ('comment', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Recommendation',
                'verbose_name_plural': 'Recommendations',
                'ordering': ['username'],
            },
        ),
    ]
