from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class Emotions_data(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Get request to fetch the data"""
        # data = mysql_connection("select * from emotions limit 1")
        # print(data)
        emotions = Emotions.objects.all()
        serializer = EmotionSerializer(emotions, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a record"""
        serializer = CreateEmotionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        else:
            return Response("Invalid")

    def put(self, request):
        """Update the record"""
        record = Emotions.objects.get(pk=request.data.get("Id"))
        serializer = UpdateEmotionSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Invalid")

    def patch(self, request):
        """Update specific fields"""
        record = Emotions.objects.get(pk=request.data.get("Id"))
        serializer = UpdateEmotionSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Invalid")

    def delete(self, request):
        """Delete Specific records"""
        record = Emotions.objects.get(pk=request.data.get("Id"))
        record.delete()
        return Response("deleted")
