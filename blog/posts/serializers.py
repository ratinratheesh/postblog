from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        fields = ('id','title','content','image','created_at','updated_at',)
        model = models.Post