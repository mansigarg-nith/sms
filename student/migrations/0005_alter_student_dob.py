# Generated by Django 3.2.7 on 2021-11-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
