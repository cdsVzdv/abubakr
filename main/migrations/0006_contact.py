# Generated by Django 5.0.3 on 2024-10-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_testimular_rasm_testimullar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adressi', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('emaiol', models.CharField(max_length=50)),
            ],
        ),
    ]
