from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from home.models import Person, Answers, Question
from home.serializers import PersonSerializer, AnswerSerializer, QuestioinSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status


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
        name = request.query_params["name"]
        return Response(data={"name": name})

    def post(self, request):
        name = request.data["name"]
        return Response(data={"name": name})


class HomeSerializerView(APIView):
    permission_classes = [
        IsAdminUser,
    ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(persons, many=True)
        return Response(data=ser_data.data)


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestioinSerializer(instance=questions, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser_data = QuestioinSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestioinSerializer(
            instance=question, data=request.data, partial=True
        )
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({"message": "question deleted"}, status=status.HTTP_200_OK)


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestioinSerializer(instance=questions, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class QuestionCreatView(APIView):
    def post(self, request):
        ser_data = QuestioinSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestioinSerializer(
            instance=question, data=request.data, partial=True
        )
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_200_OK)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({"message": "question deleted"}, status=status.HTTP_200_OK)
