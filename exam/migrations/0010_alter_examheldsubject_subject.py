# Generated by Django 3.2.7 on 2021-11-20 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_remove_teacher_username'),
        ('exam', '0009_alter_examheldsubject_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examheldsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.subject'),
        ),
    ]
