# Generated by Django 2.2.13 on 2020-07-28 20:28

from django.db import migrations

UPDATE_WATER_SUPPLY_INTENDED_WATER_USE = """
    UPDATE well SET intended_water_use_code = 'UNK' WHERE well_class_code = 'WATR_SPPLY' and intended_water_use_code = 'NA';
"""

class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0119_update_well_class_codes'),
    ]

    operations = [
        migrations.RunSQL([
            UPDATE_WATER_SUPPLY_INTENDED_WATER_USE
        ]),
    ]