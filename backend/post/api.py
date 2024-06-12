from django.http import JsonResponse

from .models import Post
from .serializers import PostSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()

    serializer = PostSerializer(posts, many= True)

    return JsonResponse({'data': serializer.data})