from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'website/home.html')

# Страница о компании
def about(request):
    company_info = {
        'Company': 'Microsoft',
        'Founded': '1975',
        'Founders': 'Bill Gates, Paul Allen',
        'Headquarters': 'Redmond, Washington, USA'
    }
    return render(request, 'website/about.html', {'company_info': company_info})

# Страница с продуктами
def products(request):
    products = ['Microsoft Windows', 'Microsoft Office', 'Azure', 'Visual Studio']
    return render(request, 'website/products.html', {'products': products})

