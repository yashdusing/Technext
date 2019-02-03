# Generated by Django 2.1.5 on 2019-01-15 13:00

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190114_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='year_of_admission',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('First', 'First Year'), ('Second', 'Second Year'), ('Third', 'Third Year'), ('Fourth', 'Fourth Year')], default='First', max_length=25),
        ),
    ]
