# Generated by Django 4.0.5 on 2022-07-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0006_mails_res_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='url_slug',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
