from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AudioFile

@api_view(['POST'])
def upload_audio(request):
    audio_file = request.FILES.get('audio')
    title = request.data.get('title')

    # Save the audio file to the database
    audio = AudioFile.objects.create(title=title, file=audio_file)

    return Response({'message': 'Audio file uploaded successfully.'})
