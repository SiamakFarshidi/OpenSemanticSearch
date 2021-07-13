# Generated by Django 3.2.3 on 2021-05-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0009_setup_url_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='graph_neo4j',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='setup',
            name='url_tasks',
            field=models.CharField(blank=True, default='http://localhost:5555/tasks', max_length=1000),
        ),
    ]