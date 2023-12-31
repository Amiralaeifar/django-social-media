# Generated by Django 4.2 on 2023-04-22 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='current_bid',
        ),
        migrations.RemoveField(
            model_name='post',
            name='bid',
        ),
        migrations.AddField(
            model_name='bids',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=8),
        ),
        migrations.AddField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='current_price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='post',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AlterField(
            model_name='bids',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.post'),
        ),
    ]
