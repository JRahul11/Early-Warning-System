# Generated by Django 3.2.6 on 2021-09-04 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_delete_pills'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pill_name', models.CharField(max_length=20)),
                ('pill_time', models.TimeField()),
                ('pill_frequency', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='pills',
            field=models.ManyToManyField(to='main_app.MedModel'),
        ),
    ]
