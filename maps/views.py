from audioop import reverse
#from binascii import a2b_hex
from django.conf import settings
from django.shortcuts import redirect, render
#from .mixins import Directions
'''
def route (request):
    context ={"google_api_key" : settings.API_KEY}
    return render(request,'maps/route.html',context)

def map(request):
    lat_a=request.GET.get('lat_a',None)
    long_a=request.GET.get('long_a',None)
    lat_b=request.GET.get('lat_b',None)
    long_b=request.GET.get('long_b',None)
    lat_c=request.GET.get('lat_c',None)
    long_c=request.GET.get('long_c',None)
    lat_d=request.GET.get('lat_d',None)
    long_d=request.GET.get('long_d',None)

    if lat_a and lat_b and lat_c and lat_d:
        directions=Directions(
            lat_a=lat_a,
            long_a=long_a,
            lat_b=lat_b,
            long_b=long_b,
            lat_c=lat_c,
            long_c=long_c,
            lat_d=lat_d,
            long_d=long_d,
        )
    else:
        return redirect(reverse('maps:route'))

    context ={
            'lat_a':lat_a,
            'long_a':long_a,
            'lat_b':lat_b,
            'long_b':long_b,
            'lat_c':lat_c,
            'long_c':long_c,
            'lat_d':lat_d,
            'long_d':long_d,
            'origin':f'{lat_a},{long_a}',
            'destination':f'{lat_b},{long_b}',
            'directions':directions,

    }
    return render(request,'maps/map.html',context)
        
'''