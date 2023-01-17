from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    # products=Product.objects.all()
   
    # n=len(products)
    # nSlides=n//4+ceil(n/4)-(n//4)
    # # params={'nSlides':nSlides, "range":range(1,nSlides),'product':products}
    # allProds=[[products, range(1, nSlides), nSlides],[products, range(1, nSlides), nSlides]]
     products= Product.objects.all()
     allProds=[]
     catprods= Product.objects.values('category', 'id')
    #  print(catprods)
     cats= {item["category"] for item in catprods}
     
     for cat in cats:
            prod=Product.objects.filter(category=cat)
            # print(prod)
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])
            params={'allProds':allProds }
            
     return render(request,'shop/index.html',params)



def about(request):
   return render(request,'shop/about.html')

def contact(request):
    if(request.method=='POST'):
        name=request.POST.get('name','')
        email=request.POST.get('name','')
        phone=request.POST.get('name','')
        desc=request.POST.get('name','')
    return render(request,'shop/contact.html')


def tracker(request):
     return render(request,'shop/tracker.html')

def search(request):
   return render(request,'shop/search.html')

def productview(request,myid):
     product=Product.objects.filter(id=myid)
     print(product)
     return render(request,'shop/productview.html',{'product':product[0]})


def checkout(request):
     return render(request,'shop/checkout.html')