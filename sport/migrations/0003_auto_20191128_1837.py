# Generated by Django 2.2.5 on 2019-11-29 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_auto_20191121_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(null=True, upload_to='staticfiles/admin/companies'),
        ),
    ]
