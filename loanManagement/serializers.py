from rest_framework import serializers
from . models import loan

class loanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = loan
        fields = ('name', 'amount')

