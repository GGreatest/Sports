from rest_framework import serializers
from models import FixtureData, PredictionData, BettingTipData

class FixtureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixtureData
        fields = '__all__'

class PredictionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionData
        fields = '__all__'

class BettingTipDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingTipData
        fields = '__all__'
