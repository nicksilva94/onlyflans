# Generated by Django 3.2.4 on 2024-07-13 00:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='contact_form_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
