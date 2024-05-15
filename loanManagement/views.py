from django.shortcuts import render
from rest_framework import viewsets
from . serializers import loanSerializer
from . models import loan

class loanViewset(viewsets.ModelViewSet):
    queryset = loan.objects.all().order_by('name')
    serializer_class = loanSerializer