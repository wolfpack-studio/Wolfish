# Generated by Django 4.0.5 on 2022-07-17 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0011_phishingdatadict_alter_phishingdata_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phishingdata',
            name='data',
        ),
        migrations.AddField(
            model_name='phishingdatadict',
            name='pdata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailer.phishingdata'),
        ),
    ]
