# Generated by Django 3.1.2 on 2020-12-05 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0003_auto_20201205_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]