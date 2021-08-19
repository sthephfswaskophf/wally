# Generated by Django 3.2.6 on 2021-08-18 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, default='0', max_digits=15, verbose_name='Avaliação')),
                ('departament_type', models.CharField(choices=[('Varejo', 'Varejo'), ('Manutenção', 'Manutenção')], default='Varejo', max_length=20)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
