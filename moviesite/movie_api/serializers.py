from rest_framework import serializers
from .models import Watchlist , StreamingPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    reviews =ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Watchlist
        fields = '__all__'

class StreamingPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True ,read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = '__all__'