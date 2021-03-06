# Generated by Django 3.2 on 2021-04-28 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('gender', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], help_text='Jenis kelamin', max_length=1, verbose_name='Gender')),
                ('phone_number', phone_field.models.PhoneField(blank=True, help_text='Phone Number', max_length=31, verbose_name='Phone Number')),
                ('mobile_number', models.CharField(blank=True, max_length=12)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('terms_of_use', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
