# Generated by Django 2.0.7 on 2018-07-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='remarks',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='备注'),
        ),
    ]
