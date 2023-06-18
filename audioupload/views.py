from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AudioFile
from .serializers import AudioFileSerializer
@api_view(['GET'])
def get_audio_by_title(request, title):
    audio_files = AudioFile.objects.filter(title__icontains=title)
    serializer = AudioFileSerializer(audio_files, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def upload_audio(request):
    audio_file = request.FILES.get('audio')
    title = request.data.get('title')

    # Save the audio file to the database
    audio = AudioFile.objects.create(title=title, file=audio_file)

    return Response({'message': 'Audio file uploaded successfully.'})
