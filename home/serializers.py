from rest_framework import serializers
from .models import Question, Answers
from .custom_relational_fields import UserNmaeEmailRelationalField


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestioinSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    # user = serializers.StringRelatedField(read_only = True)
    # user = serializers.PrimaryKeyRelatedField(read_only = True)
    # user = serializers.SlugRelatedField(read_only = True , slug_field ="email")
    user = UserNmaeEmailRelationalField(read_only = True)

    class Meta:
        model = Question
        fields = "__all__"

    def get_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Answers
        fields = "__all__"
