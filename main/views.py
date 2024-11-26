from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Index(request):
    context={
        "kirish":Kirish.objects.first(),
        "b_h":Biz_haqimizda.objects.first(),
        "b":Biz.objects.first(),
        "bs":Biz_a.objects.all(),
        "t_r":Testimular_rasm.objects.first(),
        "t":Testimullar.objects.all(),
        "con":Contact.objects.first(),
    }
    return render(request,'index.html',context)