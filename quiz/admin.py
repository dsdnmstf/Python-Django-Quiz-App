from atexit import register
from django.contrib import admin
import nested_admin
from .models import Category, Quiz, Question, Answer

class AnswerInLine(nested_admin.NestedTabularInline):
    model = Answer
    extra = 3
    max_num=6
class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInLine]
    extra = 3
    max_num=6

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer)