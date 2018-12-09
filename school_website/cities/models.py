# Create your models here.
import datetime, re
import random

from django.db import models
from django.db.models import IntegerField, Manager
from django.utils import timezone
from enum import Enum
from django.contrib.auth.models import User


class CategoryManager(models.Manager):
    def create_category(self, category):
        # category = self.create(category=re.sub('\s+', '-', category).lower())
        category = self.create(category=category)
        # do something with the category
        category.save()
        return category


class Category(models.Model):
    category = models.CharField(max_length=50, blank=False,
                                unique=True, null=True)
    # create categories with :category = Category.objects.create_category("cities")
    # objects = models.Manager()
    objects = CategoryManager()

    def __str__(self):
        return self.category


class CitiesOfTheWorld(models.Model):
    city = models.CharField(max_length=50, blank=False,
                            unique=True, null=False)
    country = models.CharField(max_length=50, blank=False,
                               unique=True, null=False)
    continent = models.CharField(max_length=50, blank=False,
                                 unique=True, null=False)

    def __init__(self, city, country, continent):
        self.city = city
        self.country = country
        self.continent = continent

    def __str__(self):
        return self.city


class ExamManager(models.Manager):
    def create_exam(self, name, allowed_time_mins=10, category=None):
        exam = self.create(name=name,
                           allowed_time_mins=allowed_time_mins,
                           category=category)
        exam.save()
        return exam


class Exam(models.Model):
    name = models.CharField(max_length=50)
    # creator = models.ForeignKey(User)
    allowed_time_mins = models.IntegerField(default=10)
    category = models.ForeignKey(
        Category, null=True, blank=True,
        on_delete=models.CASCADE)
    objects = ExamManager()

    # def add_questions(self,question):
    # question=get

    def __str__(self):
        return "--" + self.name + \
               " Allowed_time_mins:" + str(self.allowed_time_mins) + \
               " Category: " + str(self.category) + "\n"


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    # answer = models.TextField()
    # question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.answer


class QuestionManager(models.Manager):
    def question_category(self, category):
        return self.filter(category__icontains=category)

    def create_question(self, question_text, correct_answer,
                        category):
        question = self.create(question_text=question_text,
                               correct_answer=correct_answer,
                               category=category)
        return question


class Question(models.Model):
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.CASCADE)

    exams = models.ManyToManyField(Exam)
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=50)
    answer_given = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(timezone.now(), blank=True, null=True)
    answers = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=True, null=True)
    objects = QuestionManager()


    def __str__(self):
        return self.question_text

    def is_correct(self, correct_answer, answer_given):
        return correct_answer == answer_given

    def submit_answer(self, answer_given):
        self.answer_given = answer_given
        self.save()


class QuestionGenerator(models.Model):
    ''' Wrapper for Question to generate many Multiple Choice Questions
        based on input of "category" of test and number of questions
        e.g. question_predicate = "What is the capital of "
             question_subject = "Ireland"?

    '''

    def __init__(self, category, question_predicate, question_subject_list, question_choices_list,
                 num_questions_to_select=10,
                 num_choices_to_select=4):
        question_subject_list_randomized = random.sample(question_subject_list, num_questions_to_select)
        first_random_ = question_subject_list_randomized[0]
        for question_subject in question_subject_list_randomized:
            question_text = question_predicate + question_subject + "?"
            correct_answer = "dublin"
            Question(question_text, correct_answer, category)


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
