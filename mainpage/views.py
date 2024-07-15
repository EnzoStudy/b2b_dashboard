from django.shortcuts import get_object_or_404, redirect, render
from .models import Business, Performance
from .forms import BusinessForm ,PerformanceForm


def main_dashboard(request):
    # 여기에 필요한 데이터를 추가할 수 있습니다.
    context = {}
    return render(request, 'mainpage/index.html', context)

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