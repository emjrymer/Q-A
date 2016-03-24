from rest_framework import serializers
from app.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
