# Generated by Django 3.2.8 on 2021-10-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]