# Generated by Django 3.2.19 on 2023-07-05 20:48

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
