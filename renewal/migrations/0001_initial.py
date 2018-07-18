# Generated by Django 2.0.7 on 2018-07-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='项目名')),
                ('description', models.CharField(max_length=2000, null=True, verbose_name='项目描述')),
                ('last_pay_at', models.DateField(null=True, verbose_name='付款时间')),
                ('next_pay_at', models.DateField(null=True, verbose_name='到期时间')),
                ('remarks', models.CharField(max_length=3000, null=True, verbose_name='备注')),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '续费项目',
                'verbose_name_plural': '续费项目',
                'ordering': ('next_pay_at',),
            },
        ),
    ]
