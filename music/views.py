from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from rest_framework.generics import CreateAPIView, UpdateAPIView

from music.models import Music, Selection
from music.permissions import SelectionEditPermission
from music.serializers import SelectionSerializer


@method_decorator(csrf_exempt, name='dispatch')
class MusicView(View):
    def get(self, request):
        tracks = Music.objects.all()

        response = []
        for music in tracks:
            response.append(
                {
                    "id": music.id,
                    "name": music.name,
                    "audio_file": music.audio_file,
                    "durations": music.durations,
                    "info": music.info,
                }
            )
        return JsonResponse(response, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class MusicDetailView(DetailView):
    model = Music

    def get(self, request, *args, **kwargs):
        music = self.get_object()
        return JsonResponse(
            {
                "id": music.id,
                "name": music.name,
                "audio_file": music.audio_file,
                "durations": music.durations,
                "info": music.info,
            }, status=200, safe=False
        )


class SelectionView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    #permission_classes = [SelectionCreatePermission]

class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [SelectionEditPermission]



