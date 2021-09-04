# Generated by Django 3.2.2 on 2021-09-04 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_profilemodel_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pillname', models.CharField(max_length=25)),
                ('dosage', models.IntegerField()),
                ('time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profilemodel')),
            ],
        ),
    ]