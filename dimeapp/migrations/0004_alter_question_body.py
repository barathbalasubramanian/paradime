# Generated by Django 4.0.5 on 2022-07-12 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dimeapp', '0003_alter_question_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
