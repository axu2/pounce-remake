# Generated by Django 3.0.6 on 2020-05-08 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=200, unique=True)),
                ('subject', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('start_time', models.CharField(max_length=200)),
                ('end_time', models.CharField(max_length=200)),
                ('days', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pounce.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('isActive', models.BooleanField(default=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pounce.Section')),
            ],
        ),
    ]