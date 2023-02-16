from rest_framework import serializers
from .models import student

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['id', 'name','roll','city']
    # name= serializers.CharField(max_length=100)
    # roll = serializers.IntegerField()
    # city= serializers.CharField(max_length=100)
    
    # def create(self, validated_data):
    #     return student.objects.create(**validated_data)