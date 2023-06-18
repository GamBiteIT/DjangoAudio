from rest_framework import serializers
from .models import AudioFile

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ('title', 'file', 'uploaded_at')
