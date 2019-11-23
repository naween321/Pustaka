# Generated by Django 2.2.7 on 2019-11-23 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('status', models.CharField(choices=[('REQUESTED', 'requested'), ('CANCELED', 'canceled'), ('REJECTED', 'rejected'), ('DECLINED', 'declined'), ('ON_DELIVERY', 'on_delivery'), ('OFFERED', 'offered'), ('EXCHANGED', 'exchanged')], default='REQUESTED', max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='book.Book')),
                ('exchanged_with', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction_exchanged_books', to='book.Book')),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_requested_by', to=settings.AUTH_USER_MODEL)),
                ('requested_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_requested_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('status', models.CharField(choices=[('REQUESTED', 'requested'), ('CANCELED', 'canceled'), ('REJECTED', 'rejected'), ('DECLINED', 'declined'), ('ON_DELIVERY', 'on_delivery'), ('OFFERED', 'offered'), ('EXCHANGED', 'exchanged')], default='REQUESTED', max_length=20)),
                ('exchange_with', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book.Book')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]