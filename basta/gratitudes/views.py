from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from gratitudes.models import Gratitude
from gratitudes.serializers import GratitudeSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def gratitude_list(request):
    if request.method == 'GET':
        gratitudes = Gratitude.objects.all()
        serializer = GratitudeSerializer(gratitudes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GratitudeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def gratitude_detail(request, pk):
    try:
        gratitude = Gratitude.objects.get(pk=pk)
    except Gratitude.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GratitudeSerializer(gratitude)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GratitudeSerializer(gratitude, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gratitude.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
