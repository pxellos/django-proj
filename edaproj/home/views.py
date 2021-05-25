from django.shortcuts import render
from io import StringIO
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline


coin = pd.read_csv('./BitCoin.csv')
# coin = pd.read_csv(r'C:\Users\PJH\Downloads\BitCoin.csv')  # Windows Test


def return_graph():

    coin_date = (coin['Date'] >= '2016-06-01') & (coin['Date'] <= '2017-06-30')
    coin_open = coin['Open']
    coin_result = coin[coin_date & coin_open]
    coin_result = coin_result.sort_values('Date')

    fig = plt.figure(figsize=(20, 10))
    plt.plot(coin_result['Date'], coin_result['Open'], '#f2a900')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Bitcoin Moving Average')

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


# Create your views here.
def home(request):
    res = {'graph': None}
    res['graph'] = return_graph()
    return render(request, 'coin.html', res)


def index(request):
    # name = 'Michael'
    nums = [1, 2, 3, 4, 5]
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'index.html', {"my_list": nums})
