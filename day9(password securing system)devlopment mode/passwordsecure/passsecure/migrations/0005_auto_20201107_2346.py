# Generated by Django 3.1.2 on 2020-11-07 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passsecure', '0004_auto_20201107_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secure',
            name='userid',
            field=models.IntegerField(verbose_name=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='passsecure.usertable', verbose_name='')),
        ),
    ]