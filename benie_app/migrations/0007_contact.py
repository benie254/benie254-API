# Generated by Django 4.1.1 on 2022-12-30 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('benie_app', '0006_reaction_alter_project_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=220, null=True)),
                ('message', models.TextField(blank=True, max_length=9000, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
