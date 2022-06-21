from rest_framework import serializers
from .models import Category, Quiz, Answer, Question
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "quiz_count"
        )
class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = (
            "title",
            "question_count"
        )
        

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            "answer_text",
            "is_right"
        )


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            "title",
            "answer",
            "difficulty"
        )
