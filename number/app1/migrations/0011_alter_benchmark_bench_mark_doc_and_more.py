# Generated by Django 5.0.6 on 2024-10-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_balancesheetratios_cash_ratio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmark',
            name='bench_mark_doc',
            field=models.FileField(null=True, upload_to='BenchMark'),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='source',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='valuation',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='valuation_doc',
            field=models.FileField(null=True, upload_to='BenchMark'),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='valuation_dt',
            field=models.DateField(null=True),
        ),
    ]
