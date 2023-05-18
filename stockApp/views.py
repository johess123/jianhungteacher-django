from django.shortcuts import render
from django.core.paginator import Paginator

from .models import allstock, allprice

# Create your views here.i
def mainPage(request):
    return render(request, 'main.html',context)

def cp(request):
    stockList = allprice.objects.all()
    stockList1 = []
    for i in range(len(stockList)):
        stockname = allstock.objects.filter(stockid=stockList[i].stockid)
        #print(stockname[0].stockname)
        stockList1.append({"id":stockList[i].id,"stockid":stockList[i].stockid,"stockname":stockname[0].stockname,"date":stockList[i].date,"price":stockList[i].price/100})
    paginator = Paginator(stockList1,50)
    pageNum = request.GET.get('page')
    thisPage = paginator.get_page(pageNum)
    context = {
        'stockList':thisPage, 
    }
    return render(request, 'showcp.html',context)

# tocay close price
def today(request):
    stockList = allprice.objects.all()
    stockList1 = []
    for i in range(len(stockList)):
        stockname = allstock.objects.filter(stockid=stockList[i].stockid)
        stockList1.append({"id":stockList[i].id,"stockid":stockList[i].stockid,"stockname":stockname[0].stockname,"datte":stockList[i].date,"price":stockList[i].price/100})
    context = {
        'stockList':stockList1,
    }
    return render(request,'.html',context)
# choose day close price
def chooseday(request):
    print("choose")
# all stock close price
def ascp(request):
    print("ascp")
# choose stock close price
def cscp(request):
    print("cscp")
# finstate
def fi(request):
    print("finstate")

