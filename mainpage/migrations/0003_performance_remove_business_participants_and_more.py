# Generated by Django 5.0.7 on 2024-07-15 14:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainpage", "0002_alter_business_period_end_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Performance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("participants", models.IntegerField()),
                ("period_start", models.CharField(max_length=50)),
                ("period_end", models.CharField(max_length=50)),
                ("result", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="business",
            name="participants",
        ),
        migrations.RemoveField(
            model_name="business",
            name="period_end",
        ),
        migrations.RemoveField(
            model_name="business",
            name="period_start",
        ),
        migrations.RemoveField(
            model_name="business",
            name="result",
        ),
        migrations.AddField(
            model_name="business",
            name="budget",
            field=models.DecimalField(
                decimal_places=2, default=0.0, max_digits=15, verbose_name="사업금액"
            ),
        ),
        migrations.AddField(
            model_name="business",
            name="expected_order_date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="발주예정일"
            ),
        ),
        migrations.AddField(
            model_name="business",
            name="is_strategic",
            field=models.BooleanField(default=False, verbose_name="전략사업여부"),
        ),
        migrations.AddField(
            model_name="business",
            name="proposal_pm",
            field=models.CharField(default="홍길동", max_length=100, verbose_name="제안PM"),
        ),
        migrations.AddField(
            model_name="business",
            name="sales_division",
            field=models.CharField(default="None", max_length=100, verbose_name="영업본부"),
        ),
        migrations.AddField(
            model_name="business",
            name="sales_representative",
            field=models.CharField(default="홍길동", max_length=100, verbose_name="영업대표"),
        ),
        migrations.AlterField(
            model_name="business",
            name="name",
            field=models.CharField(max_length=200, verbose_name="사업명"),
        ),
    ]
