# Generated by Django 2.1 on 2018-09-19 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('twilio_call_id', models.CharField(blank=True, max_length=64, null=True)),
                ('caller_number', models.CharField(blank=True, max_length=32, null=True)),
                ('caller_name', models.CharField(blank=True, max_length=32, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(db_index=True, max_length=32)),
                ('forwarding_number', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='calls',
            name='number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='calls', to='voip.Number'),
        ),
    ]
