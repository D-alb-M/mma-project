# Generated by Django 5.0.4 on 2024-05-09 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('info', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='fighter',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mma.division'),
        ),
        migrations.AddField(
            model_name='fight',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mma.section'),
        ),
    ]