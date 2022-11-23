# Generated by Django 2.2.8 on 2020-01-07 18:21

from django.db import migrations

updateAquiferSimplifiedGeom = """
    UPDATE aquifer SET geom_simplified=ST_Simplify(ST_Transform(geom, 4326), 0.0005) WHERE geom_simplified IS NULL
"""

class Migration(migrations.Migration):

    dependencies = [
        ('aquifers', '0026_auto_20191216_2135'),
    ]

    operations = [
        migrations.RunSQL(
            [updateAquiferSimplifiedGeom],
        )
    ]
