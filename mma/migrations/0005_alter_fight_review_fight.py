# Generated by Django 5.0.4 on 2024-05-16 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mma', '0004_bout_fight_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fight_review',
            name='fight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fight_reviews', to='mma.fight'),
        ),
    ]
