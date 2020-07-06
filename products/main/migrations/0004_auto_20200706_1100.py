# Generated by Django 3.0.8 on 2020-07-06 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200706_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aliment',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='UpdateDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField()),
                ('aliment_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Aliment')),
            ],
        ),
    ]
