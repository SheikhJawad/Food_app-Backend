# Generated by Django 5.1.3 on 2024-11-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_childitem_parentcategory_delete_menuitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childitem',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='parentcategory',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
