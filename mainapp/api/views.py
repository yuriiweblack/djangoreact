from rest_framework import viewsets

from .serializers import BlogCategorySerializer, BlogPostSerializer, BlogPostListRetrieveSerializer
from ..models import BlogCategory, BlogPost


class BlogCategoryViewSet(viewsets.ModelViewSet):

    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogPostViewSet(viewsets.ModelViewSet):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    action_to_serializer = {
        "list": BlogPostListRetrieveSerializer,
        "retrieve": BlogPostListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )



# class TestAPIView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         data = [{"id": 1, "name": "Jone"}, {"id":2, "name": "Mark"}]
#         return Response(data)
