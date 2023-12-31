# Generated by Django 4.1.1 on 2023-12-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('box_type', models.CharField(choices=[('premium', 'Premium'), ('common', 'Common')], max_length=15, primary_key=True, serialize=False)),
                ('new_boxes', models.IntegerField(default=0)),
                ('qtt_total', models.IntegerField(default=0)),
                ('box_qtt', models.IntegerField(default=0)),
                ('damaged_box_qtt', models.IntegerField(default=0)),
                ('borrowed_producer', models.IntegerField(default=0)),
                ('borrowed_merchant', models.IntegerField(default=0)),
            ],
        ),
    ]
