from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from home.models import Person
from home.serializers import PersonSerializer


@api_view(["GET", "POST", "PUT"])
def home(request):
    return Response({"name": "sss"})


class HomeView(APIView):
    def get(self, request):
        return Response(data={"name": "sss class base view"})


class NameView(APIView):
    def get(self, request, name):
        return Response(data={"name": name})


class NameParamsView(APIView):
    def get(self, request):
        # name = request.GET['name']
        name = request.query_params['name']
        return Response(data={"name": name})
    
    def post(self , request):
        name = request.data['name']
        return Response(data={"name": name})


class HomeSerializerView(APIView):
    def get(self , request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(persons , many= True )
        return Response(data=ser_data.data)
