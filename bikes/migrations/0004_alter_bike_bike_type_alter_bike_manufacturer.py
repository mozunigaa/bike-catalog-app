# Generated by Django 4.0.3 on 2022-03-11 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0003_rename_typebike_biketype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='bike_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bike', to='bikes.biketype'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bike', to='bikes.manufacturer'),
        ),
    ]