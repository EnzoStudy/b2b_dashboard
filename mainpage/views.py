import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum, F, Func, Count
from django.db.models.functions import TruncMonth


from .models import Business, Performance
from .forms import BusinessForm ,PerformanceForm



def get_monthly_business_data(dataset):
      
    today = datetime.date.today()
    year = today.year
    month = today.month


    # 각 월별 값 확인
    business_monthly_stats = dataset.objects.annotate(
        month=TruncMonth('expected_order_date')
    ).values('month').annotate(
        total_budget=Sum('budget'),
        total_count=Count('id')
    ).order_by('month')
    
    
    # 이전 달, 현재 달, 이후 달 구하기
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year

    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

    # business_monthly_stats 에서 필요한 정보 추출
    prev_month_data = next(filter(lambda x: x['month'].year == prev_year and x['month'].month == prev_month, business_monthly_stats), None)
    curr_month_data = next(filter(lambda x: x['month'].year == year and x['month'].month == month, business_monthly_stats), None)
    next_month_data = next(filter(lambda x: x['month'].year == next_year and x['month'].month == next_month, business_monthly_stats), None)

    # 딕셔너리에 저장
    neighbor_stats = {
        'prev_month': {
            'total_budget': prev_month_data['total_budget'] if prev_month_data else 0,
            'total_count': prev_month_data['total_count'] if prev_month_data else 0
        },
        'curr_month': {
            'total_budget': curr_month_data['total_budget'] if curr_month_data else 0,
            'total_count': curr_month_data['total_count'] if curr_month_data else 0
        },
        'next_month': {
            'total_budget': next_month_data['total_budget'] if next_month_data else 0,
            'total_count': next_month_data['total_count'] if next_month_data else 0
        }
    }

    return business_monthly_stats, neighbor_stats


def main_dashboard(request):
    # 여기에 필요한 데이터를 추가할 수 있습니다.
    
   
  
    business_monthly_stats, neighbor_stats = get_monthly_business_data(Business)
   
    
    for i in business_monthly_stats:
        print(i)
    # print(business_monthly_stats)
    print(neighbor_stats)
    

        
        
    
    return render(request, 'mainpage/index.html', {'neighbor_stats':neighbor_stats, 'business_monthly_stats':business_monthly_stats} )
    
    # return render(request, 'mainpage/index.html', {'businesses': businesses})


##############################################################
########################## 역량 영역  ##########################
##############################################################

def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'mainpage/performance_list.html', {'performances': performances})

def create_performance(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'mainpage/performance_form.html', {'form': form})

def update_performance(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        form = PerformanceForm(request.POST, instance=performance)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm(instance=performance)
    return render(request, 'mainpage/performance_form.html', {'form': form})



##############################################################
######################## 비즈니스 영역  #########################
##############################################################


def business_list(request):
    businesses = Business.objects.all()
    return render(request, 'mainpage/business_list.html', {'businesses': businesses})



def create_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm()
    return render(request, 'mainpage/business_form.html', {'form': form})

def update_business(request, pk):
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            return redirect('business_list')
    else:
        form = BusinessForm(instance=business)
    return render(request, 'mainpage/business_form.html', {'form': form})