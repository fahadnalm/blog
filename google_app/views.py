from django.shortcuts import render
from django.http import JsonResponse
import requests

def text_search(request):
    API_KEY = "AIzaSyA2rUPhyOxI59ytFZZm-AIifOS6PryPMH8"
    query = request.GET.get("text", '')
    next_page_token = request.GET.get("next_page_token")

    TEXT_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+API_KEY

    if next_page_token is not None:
       TEXT_SEARCH_URL += "&pagetoken=" + next_page_token


    response = requests.get(TEXT_SEARCH_URL)

    context = {
    	"response": response.json(),
    }
    return render(request, 'text_search.html', context)

    return JsonResponse(response.json(), safe=False)

def place_detail(request):
    API_KEY = "AIzaSyCZLaHVXb1noZMzx0OIwpotV9QY-9EK_l0"
    reference = request.GET.get("reference", "")

    PLACE_ID_URL = "https://maps.googleapis.com/maps/api/place/details/json?reference="+reference+"&key="+API_KEY
    response = requests.get(PLACE_ID_URL)

    context = {
    	"response": response.json()
    }
    return render(request, 'place_detail.html', context)

    return JsonResponse(response.json(), safe=False)
