from rest_framework.serializers import ModelSerializer
from .models import dbNote

# Model Serialiser
class noteSerializer(ModelSerializer):
    class Meta:
        model = dbNote
        fields = '__all__'