# Generated by Django 2.0.4 on 2019-05-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managecenter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='url',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='website',
            name='describe',
            field=models.TextField(blank=True, null=True),
        ),
    ]
