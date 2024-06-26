from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Snippets
from .serializers import SnippetSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

# listing all existing snippets or creating a new snippet
@api_view(['GET', 'POST'])
def snippet_list(request):

    if request.method == 'GET':
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = SnippetSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
# listing an instance of a snippet or updating and deleting an instance of a snippet

@api_view(['GET','PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet = get_object_or_404(Snippets, pk = pk)
    except Snippets.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = SnippetSerializer(snippet, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
        