# Generated by Django 4.1.3 on 2022-12-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_gender_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-Binary', 'Non-Binary')], default='Male', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Status',
            field=models.CharField(choices=[('Not Committed', 'Not Committed'), ('Committed', 'Committed')], default='Not Committed', max_length=50),
        ),
    ]