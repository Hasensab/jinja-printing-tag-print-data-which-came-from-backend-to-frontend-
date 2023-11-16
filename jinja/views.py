from django.shortcuts import render

# Create your views here.
data='hey handsome Hasen'
d={'assumption':data}
def hasen(request):
    return render(request,'hasen.html',context=d)
