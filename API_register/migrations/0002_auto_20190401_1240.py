# Generated by Django 2.1.8 on 2019-04-01 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='classes',
            new_name='student_class',
        ),
    ]