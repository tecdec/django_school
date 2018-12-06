from math import pi
from pprint import pprint

from django.test import TestCase
import inspect
import logging
from .models import Exam, Category, Question, Answer,CitiesOfTheWorld, QuestionGenerator

class CitiesOfTheWorldTests(TestCase):
    def setUp(self):
        CitiesOfTheWorldTests("Dublin","Ireland","Europe")
        CitiesOfTheWorldTests("London","England","Europe")
        CitiesOfTheWorldTests("Paris","France","Europe")
        CitiesOfTheWorldTests("Berlin","Germany","Europe")
        CitiesOfTheWorldTests("Stockholm","Sweden","Europe")
        CitiesOfTheWorldTests("Helsinki","Finland","Europe")
        CitiesOfTheWorldTests("Talin","Finland","Europe")
        CitiesOfTheWorldTests("Belfast","Northern Ireland","Europe")



class CategoryModelTests(TestCase):
    categories = None

    def setUp(self):
        Category.objects.create_category("European Capital Cities")
        Category.objects.create_category("Capital Cities")
        Category.objects.create_category("test_delete")
        self.categories = Category.objects.all()

    def test_creation_of_new_category(self):
        # Category.objects.create_category("European Capital Cities")
        # Category.objects.create_category("Capital Cities")
        # categories = Category.objects.all()
        self.assertEqual("European Capital Cities", str(self.categories[0]))
        self.assertEqual("Capital Cities", str(self.categories[1]))

    def test_delete_of_category(self):
        # print(str(self.categories.filter(category="test_delete")) + "rrrrrrrrr")
        # print("ooo:" + str(self.categories.filter(name="test_delete")))
        print(str(inspect.stack()[0][3]) + str(self.categories.get(category__exact="test_delete")))


class ExamModelTests(TestCase):
    def setUp(self):
        CategoryModelTests.setUp(self)
        Exam.objects.create_exam(name="European Capital Cities", allowed_time_mins=20)
        Exam.objects.create_exam(name="footy Cities", allowed_time_mins=440)
        Exam.objects.create_exam(name="swimming Cities")
        Exam.objects.create_exam(name="cycling Cities",
                                 category=Category.objects.create_category("Irish Cities")
                                 )
        Exam.objects.create_exam(name="ffff Cities",
                                 category=Category.objects.all()[1]
                                 )

    def test_creation_of_new_exam(self):
        """
        determine if exam can be created by user
        """
        print("def " + str(inspect.stack()[0][3]))
        exam = Exam.objects.all()[0]
        self.assertEqual("European Capital Cities", str(exam.name))
        # exam.category=cities
        # cities = Category.objects.create_category("European Capital Cities")
        print(Category.objects.all())
        print(str(Exam.objects.all()))
        print(exam)
        print("_-_-_-_-_-")
        assert (True)

    def test_add_tests_to_exam(self):
        assert (True)


class QuestionModelTests(TestCase):
    # answers = None

    def setUp(self):
        self.assertNotEquals(3.14, pi)
        print("def " + str(inspect.stack()[0][3]))
        # CategoryModelTests.setUp(self)
        Category.objects.create_category("European Capital Cities")
        Category.objects.create_category("Capital Cities")
        Category.objects.create_category("test_delete")
        # self.questions = set()
        # self.answers = set()
        self.categories = Category.objects.all()
        q1 = Question(question_text="What is the capital of Ireland", correct_answer="Dublin",
                      category=self.categories[0])
        q2 = Question(question_text="What is the capital of Northern Ireland", correct_answer="Belfast",
                      category=self.categories[0])
        q3 = Question(question_text="What is the capital of Iceland", correct_answer="Reykjavik",
                      category=self.categories[0])
        q4 = Question(question_text="What is the capital of Estonia", correct_answer="Talin",
                      category=self.categories[0])
        a1 = Answer(answer="Dublin")
        a2 = Answer(answer="Belfast")
        # pprint(vars(q1))
        q1.save()
        q2.save()
        q3.save()
        a1.save()
        a2.save()
        self.questions = Question.objects.all()
        self.answers = Answer.objects.all()
        self.assertEqual(Question.objects.count(), 3, msg="found wrong number of questions")
        self.assertEqual(self.answers.count(), 2, msg="found wrong number of answers")

    def test_show_questions(self):
        print("def " + str(inspect.stack()[0][3]))
        for question in self.questions:
            print("question : " + str(question))

    def test_show_answers(self):
        print("def " + str(inspect.stack()[0][3]))
        for choice in self.answers:
            print("print choice : " + str(choice))

    def test_answering_questions(self):
        """in def test_answering_questions
        for question in questions:
            assert that answer_given is None before answer_given is submitted
            submit_answer
            assert that answer_given =  correct_answer
            assert that answer_given !=  correct_answer
        """

        print("def " + str(inspect.stack()[0][3]))
        self.assertEqual(self.answers.count(), 2, msg="found wrong number of answers")

        for question in self.questions:
            # print('now about to execute : -self.questions[0].submit_answer("XXXXXX")' + "\n ##################")
            # pprint(vars(Question.objects.all().get(pk=int(question.id))))
            self.assertFalse(question.answer_given, msg="the answer_given=None")
            # assert that first answer_given is correct
            question.submit_answer("Dublin")

        #    assert that last answer_given in iteration above is incorrect
        question = Question.objects.all().get(pk=3)
        self.assertNotEqual(question.answer_given, question.correct_answer)
        self.assertFalse(question.is_correct(question.correct_answer, question.answer_given),
                         msg="def is_correct is incorrect!")
        # print('just executed : -self.questions[0].submit_answer("Dublin")' + "\n ##################")


    def print_objects_attributes(self):
        for question in self.questions:
            print('now about to execute : -self.questions[0].submit_answer("YYYYYYYY")' + "\n ##################")
            pprint(vars(Question.objects.all()))
            pprint(vars(Question.objects.all().get(pk=int(question.id))))
        for question in self.questions:
            print("question : " + str(question))

class QuestionGeneratorTests(TestCase,CitiesOfTheWorldTests):
    def setUp(self):
        country_list=CitiesOfTheWorldTests.country.column
        question_choices_list=CitiesOfTheWorldTests.city.column
        QuestionGenerator("European Capital Cities","What is the capital of ", country_list,
                        question_choices_list,num_questions_to_select=5, num_choices_to_select=6)

