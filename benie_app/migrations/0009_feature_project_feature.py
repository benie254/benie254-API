# Generated by Django 4.1.1 on 2023-01-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benie_app', '0008_alter_project_short_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='feature',
            field=models.ManyToManyField(to='benie_app.feature'),
        ),
    ]
