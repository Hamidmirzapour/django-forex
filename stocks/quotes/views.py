from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Portfolio
from .forms import PortfolioForm

def home(request):
    import json
    import requests

    if request.method == 'POST':
        base = request.POST['base']
        quote = request.POST['quote']
        api_request = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' + base + '&to_currency=' + quote + '&apikey=67EJG7UPIFKBYNXA')
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error ...'

        from_currency_symbol = api['Realtime Currency Exchange Rate']['1. From_Currency Code']
        from_currency_name = api['Realtime Currency Exchange Rate']['2. From_Currency Name']
        to_currency_symbol = api['Realtime Currency Exchange Rate']['3. To_Currency Code']
        to_currency_name = api['Realtime Currency Exchange Rate']['4. To_Currency Name']
        exchange_rate = api['Realtime Currency Exchange Rate']['5. Exchange Rate']
        last_updated = api['Realtime Currency Exchange Rate']['6. Last Refreshed']
        ask_price = api['Realtime Currency Exchange Rate']['9. Ask Price']
        bid_price = api['Realtime Currency Exchange Rate']['8. Bid Price']
        
        return render(request, 'home.html', { 'api': api,
        'from_currency_symbol': from_currency_symbol,
        'to_currency_symbol': to_currency_symbol,
        'from_currency_name': from_currency_name,
        'to_currency_name': to_currency_name,
        'exchange_rate': exchange_rate,
        'last_updated': last_updated,
        'ask_price': ask_price,
        'bid_price': bid_price,
        })
    else:
        return render(request, 'home.html', {'message': 'Please Enter the Base and Quote Currency Above.'})
    

def about(request):
    return render(request, 'about.html', {})

def portfolio(request):
    import requests
    import json

    if request.method == 'POST':
        form = PortfolioForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, (f'The \"{request.POST["base_currency"]}/{request.POST["quote_currency"]}\" has been added to portfolio successfully!'))
            return redirect('portfolio')
        else:
            return redirect('portfolio')
    else:
        portfolio = Portfolio.objects.all()
        output = []
        for portfo in portfolio:
            base, quote = (str(portfo)).split('/')
            api_request = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' + str(base) + '&to_currency=' + str(quote) + '&apikey=67EJG7UPIFKBYNXA')
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = 'Error ...'

        return render(request, 'portfolio.html', { 'portfolio': portfolio, 'output': output, 'portfolio': portfolio})

def delete(request, portfo_id):
    portfo = Portfolio.objects.get(pk=portfo_id)
    portfo.delete()
    messages.success(request, (f'The "{portfo}" has been deleted from portfolio successfully!'))
    return redirect('portfolio')
