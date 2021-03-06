# Generated by Django 4.0.2 on 2022-03-19 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('body', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=120)),
                ('state', models.BooleanField()),
                ('questionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.question')),
            ],
        ),
    ]
