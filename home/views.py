from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    peoples=[
        {'Name':"Nabeel Akhtar","Age":24},
        {'Name':"Adeel Akhtar","Age":20},
        {'Name':"Waleed Akhtar","Age":14},
        {'Name':"Abdullah","Age":24},
        {'Name':"Fuzail","Age":26},
    ]
    context={'peoples':peoples}
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')