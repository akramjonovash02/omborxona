# Generated by Django 5.0.5 on 2024-05-09 01:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotuv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.FloatField()),
                ('summa', models.FloatField()),
                ('tolandi', models.FloatField(default=0)),
                ('qarz', models.FloatField(default=0)),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('mahsulot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.mahsulot')),
                ('mijoz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.mijoz')),
                ('tarqatuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
