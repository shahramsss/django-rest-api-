from rest_framework import serializers
from .models import Question, Answers


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestioinSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = "__all__"

    def get_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"
