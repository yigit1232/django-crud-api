from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

@api_view(['GET'])
def index(request):
    if request.method=='GET':
        return Response(
            {
                'Post All':'http://127.0.0.1:8000/api/post/list/',
                'Post Detail':'http://127.0.0.1:8000/api/post/detail/<slug:slug>/',
                'Post Create':'http://127.0.0.1:8000/api/post/create/',
                'Post Update': 'http://127.0.0.1:8000/api/post/update/<int:id>/',
                'Post Delete':'http://127.0.0.1:8000/api/post/delete/<int:id>/'
            }
        )
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_all_post(request):
    if request.method=='GET':
        data = Post.objects.all().order_by('-created_at')
        if not data:
            return Response({'null':'There are no posts'},status=status.HTTP_204_NO_CONTENT)
        serializer = PostSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_detail_post(request,slug):
    if request.method=='GET':
        try:
            data = Post.objects.get(slug=slug)
            serializer = PostSerializer(data)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'404':'Post not found'},status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def post_create(request):
    if request.method=='POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            content = serializer.validated_data['content']
            post = Post(title=title,content=content)
            post.save()
            return Response({'created':'Post created','data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class post_update(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

@api_view(['DELETE'])
def post_delete(request,id):
    if request.method=='DELETE':
        try:
            data = Post.objects.get(id=id)
            data.delete()
            return Response({'deleted':'Post delete'},status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'404': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

