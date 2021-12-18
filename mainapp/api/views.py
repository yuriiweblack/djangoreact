from rest_framework.views import APIView
from rest_framework.response import Response


class TestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [{"id": 1, "name": "Jone"}, {"id":2, "name": "Mark"}]
        return Response(data)
