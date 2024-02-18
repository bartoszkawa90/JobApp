from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import JobOffer
from .Logger import Logger
from .serializers import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


#   TE DWIE TU NIZEJ SA DO REST API I CHODZIW  NICH O TO ZE JEST TO OPIS CO SIE MA DZIAC PRZY REQUESTACH NA GET POST PUT I DELETE
#   I JEST USTAWIONE POD WCZESNIEJ ZROBIONY MODEL BAZY
@api_view(['GET', 'POST'])
def joboffer_list(request):
    if request.method == 'GET':
        all_offers = JobOffer.objects.all()
        serializer = JobOfferSerializer(all_offers, context={'request': request}, many=True)
        Logger.info(f'GET request {serializer.data}')
        return Response(serializer.data)

    elif request.method == 'POST':   # w POST należy sprawdzić czy wszystkie dane zgadzają sie z modelem
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Logger.info(f'POST request {serializer.data}')
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def joboffer_detail(request, pk):
    try:
        offer = JobOffer.objects.get(pk=pk)
    except JobOffer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = JobOfferSerializer(offer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            Logger.info(f'PUT request {serializer.data}')
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        offer.delete()
        Logger.info(f'DELETE request {offer.data}')
        return Response(status=status.HTTP_204_NO_CONTENT)
