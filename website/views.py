from django.shortcuts import render


# pass VJ9673457589 vaishnavi7818    Vaishnavi9673457589  vaishu7818

# Create your views here.
def base(request): 
    return render(request,'base.html')
#def index(request):
 #   return render(request,'index.html')
    #return HttpResponse("This is home page")
def cart(request):
    return render(request,'cart.html')
def login(request):
    return render(request,'login.html')        