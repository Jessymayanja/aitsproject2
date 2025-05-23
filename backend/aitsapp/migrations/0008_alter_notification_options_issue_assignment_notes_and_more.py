# Generated by Django 5.1.5 on 2025-04-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aitsapp', '0007_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='issue',
            name='assignment_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='resolution_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
