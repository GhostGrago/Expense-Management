# Generated by Django 4.2.3 on 2023-07-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0028_alter_family_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
