# your_app/management/commands/generate_business.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from mainpage.models import Business
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Generates 500 random business entries'

    def handle(self, *args, **kwargs):
        business_names = [
            "테크노솔루션", "스마트시스템즈", "이노베이션랩", "퓨처테크", "디지털파워",
            "네트워크플러스", "클라우드엑스", "AI솔루션스", "빅데이터그룹", "모바일존",
            "사이버시큐리티", "로보틱스프로", "VR익스피리언스", "IoT커넥트", "블록체인테크",
            "그린에너지솔루션", "스마트팩토리", "핀테크이노베이션", "헬스케어테크", "에듀테크플랫폼"
        ]

        sales_divisions = ["금융고객", "전략고객", "biz고객", "공공고객", "기타"]

        for _ in range(500):
            name = f"{random.choice(business_names)} 프로젝트 {random.randint(1, 100)}"
            start_date = timezone.datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
            budget = round(random.uniform(1, 1000), 2)
            sales_representative = f"영업사원{random.randint(1, 20)}"
            sales_division = random.choice(sales_divisions)
            proposal_pm = f"PM{random.randint(1, 10)}"
            is_strategic = random.choice([True, False])
            business_type = random.choice(['신규', '재계약','탈환'])

            Business.objects.create(
                name=name,
                expected_order_date=start_date,
                budget=budget,
                sales_representative=sales_representative,  # 'sales_rep' -> 'sales_representative'
                sales_division=sales_division,
                proposal_pm=proposal_pm,
                is_strategic=is_strategic,
                business_type=business_type
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 500 random business entries'))


    
