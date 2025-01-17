# Generated by Django 5.1.3 on 2024-12-20 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_no', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('deptname', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('salary', models.PositiveBigIntegerField()),
                ('mgr', models.PositiveBigIntegerField()),
                ('comm', models.PositiveBigIntegerField()),
                ('hiredate', models.DateField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
