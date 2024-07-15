from django.db import models
from django.utils import timezone

class Performance(models.Model):
    name = models.CharField(max_length=200)
    participants = models.IntegerField()
    period_start = models.CharField(max_length=50)
    period_end = models.CharField(max_length=50)
    result = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    



class Business(models.Model):
    name = models.CharField(max_length=200, verbose_name="사업명")
    expected_order_date = models.DateField(default=timezone.now,verbose_name="발주예정일")
    budget = models.DecimalField(max_digits=15, decimal_places=2,default=0.0, verbose_name="사업금액")
    sales_representative = models.CharField(max_length=100,default='홍길동', verbose_name="영업대표")
    sales_division = models.CharField(max_length=100,default='None', verbose_name="영업본부")
    proposal_pm = models.CharField(max_length=100, default='홍길동', verbose_name="제안PM")
    is_strategic = models.BooleanField(default=False, verbose_name="전략사업여부")

    def __str__(self):
        return self.name



