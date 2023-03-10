# Generated by Django 3.2.8 on 2021-10-21 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0004_student_username'),
        ('teacher', '0009_auto_20211021_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('classSection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.classsection')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exam.exam')),
                ('stu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.student')),
            ],
        ),
    ]
