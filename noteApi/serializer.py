from rest_framework.serializers import ModelSerializer
from .models import Note

# Model Serialiser
class noteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'