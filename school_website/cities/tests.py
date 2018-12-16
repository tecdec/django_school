from math import pi
from pprint import pprint

from django.test import TestCase
import inspect
import logging
from .models import Exam, Category, Question, Answer, CitiesOfTheWorld

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def logPoint(context):
    '''utility function used for module functions and class methods'''
    callingFunction = inspect.stack()[1][3]
    logging.debug('in %s - %s()' % (context, callingFunction))


def setUpModule():
    '''called once, before anything else in this module'''
    logPoint('module %s' % __name__)
    city_list = [ ]
    city_list.append(CitiesOfTheWorld.objects.create_city("Dublin", "Ireland", "Europe"))
    city_list.append(CitiesOfTheWorld.objects.create_city("London", "England", "Europe"))
    city_list.append(CitiesOfTheWorld.objects.create_city("Paris", "France", "Europe"))
    city_list.append(CitiesOfTheWorld.objects.create_city("Berlin", "Germany", "Europe"))
    city_list.append(CitiesOfTheWorld.objects.create_city("Stockholm", "Sweden", "Europe"))
    city_list.append(CitiesOfTheWorld.objects.create_city("Helsinki", "Finland", "Europe"))
    city_list.append(CitiesOfTheWorld.objects.create_city("Talin", "Estonia", "Europe"))
    city_list.append(CitiesOfTheWorld.objects.create_city("Belfast", "Northern Ireland", "Europe"))
    for city in city_list:
        city.save()
    category_list = [ ]
    category_list.append(Category.objects.create_category("European Capital Cities"))
    category_list.append(Category.objects.create_category("Capital Cities"))
    category_list.append(Category.objects.create_category("test_delete"))
    for category in category_list:
        category.save()
    logging.debug("in " + str(inspect.stack()[0][3]) + " category = " + str(Category.objects.get(pk=1)))


def tearDownModule():
    'called once, after everything else in this module'
    logPoint('module %s' % __name__)


class CategoryModelTests(TestCase):
    categories = None

    def setUp(self):
        self.logPoint()
        self.categories = Category.objects.all()

    def test_creation_of_new_category(self):
        self.logPoint()
        # Category.objects.create_category("European Capital Cities")
        # Category.objects.create_category("Capital Cities")
        self.assertEqual("European Capital Cities", str(self.categories.get(category__exact="European Capital Cities")))
        self.assertEqual("Capital Cities", str(self.categories[1]))

    def test_delete_of_category(self):
        self.logPoint()
        # print(str(self.categories.filter(category="test_delete")) + "rrrrrrrrr")
        # print("ooo:" + str(self.categories.filter(name="test_delete")))
        # print(str(inspect.stack()[0][3]) + " " + str(self.categories.get(category__exact="test_delete")))

    def logPoint(self):
        'utility method to trace control flow'
        callingFunction = inspect.stack()[1][3]
        currentTest = self.id().split('.')[-1]
        logging.debug('in %s - %s()' % (currentTest, callingFunction))


class ExamModelTests(TestCase):
    def setUp(self):
        self.logPoint()
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
        self.logPoint()
        exam = Exam.objects.all()[0]
        self.assertEqual("European Capital Cities", str(exam.name))
        logging.debug("in " + str(inspect.stack()[0][3]) + " categories = " + str(Category.objects.all()))
        logging.debug("in " + str(inspect.stack()[0][3]) + " exams = " + str(Exam.objects.all()))
        logging.debug("in " + str(inspect.stack()[0][3]) + " exam = " + str(exam))

    def test_add_tests_to_exam(self):
        self.logPoint()

    def logPoint(self):
        '''utility method to trace control flow'''
        callingFunction = inspect.stack()[1][3]
        currentTest = self.id().split('.')[-1]
        logging.debug('in %s - %s()' % (currentTest, callingFunction))


class QuestionModelTests(TestCase):
    # answers = None
    categories = []

    def setUp(self):
        self.logPoint()
        self.assertNotEquals(3.14, pi)
        categories = Category.objects.all()
        if logger.isEnabledFor(logging.DEBUG):
            logging.debug("in " + str(inspect.stack()[0][3]) + " categories = " + str(Category.objects.all()))
            for category in categories:
                print("     category = " + str(category))
        q1 = Question.objects.create_question(question_text="What is the capital of Ireland", correct_answer="Dublin",
                                              category=categories[0])
        q2 = Question(question_text="What is the capital of Northern Ireland", correct_answer="Belfast",
                      category=categories[0])
        q3 = Question(question_text="What is the capital of Iceland", correct_answer="Reykjavik",
                      category=categories[0])
        q4 = Question(question_text="What is the capital of Estonia", correct_answer="Talin",
                      category=categories[0])
        a1 = Answer(answer="Dublin")
        a2 = Answer(answer="Belfast")
        if logger.isEnabledFor(logging.DEBUG):
            pprint(vars(q1))
        q1.save()
        q2.save()
        q3.save()
        a1.save()
        a2.save()
        self.questions = Question.objects.all()
        self.answers = Answer.objects.all()
        self.assertEqual(Question.objects.count(), 3, msg="found wrong number of questions")
        self.assertEqual(self.answers.count(), 2, msg="found wrong number of answers")
        self.logPoint()

    def test_show_questions(self):
        self.logPoint()
        # print("def " + str(inspect.stack()[0][3]))
        if logger.isEnabledFor(logging.DEBUG):
            for question in self.questions:
                print("in " + str(inspect.stack()[0][3]) + ": question : " + str(question))

    def test_show_answers(self):
        self.logPoint()
        # print("def " + str(inspect.stack()[0][3]))
        if logger.isEnabledFor(logging.DEBUG):
            for choice in self.answers:
                print("in " + str(inspect.stack()[0][3]) + ": print answer given : " + str(choice))

    def test_answering_questions(self):
        """in def test_answering_questions
        for question in questions:
            assert that answer_given is None before answer_given is submitted
            submit_answer
            assert that answer_given =  correct_answer
            assert that answer_given !=  correct_answer
        """
        self.logPoint()
        # print("def " + str(inspect.stack()[0][3]))
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
        logging.debug("in " + str(inspect.stack()[0][
                                      3]) + 'just executed : -self.questions[0].submit_answer("Dublin")' + "\n ##################")

        self.logPoint()

    def print_objects_attributes(self):
        self.logPoint()
        for question in self.questions:
            pprint(vars(Question.objects.all()))
            pprint(vars(Question.objects.all().get(pk=int(question.id))))
        for question in self.questions:
            logging.debug("question : " + str(question))

    def logPoint(self):
        """utility method to trace control flow"""
        callingFunction = inspect.stack()[1][3]
        currentTest = self.id().split('.')[-1]
        logging.debug('in %s - %s()' % (currentTest, callingFunction))

# class QuestionGeneratorTests(TestCase):
#     def setUp(self):
#         self.logPoint()
#         logging.debug("in " + str(inspect.stack()[0][3]) + " ???? = " + str(CitiesOfTheWorld.objects.all()))
#
#         city_list = list(CitiesOfTheWorld.objects.all())
#         country_list = list(CitiesOfTheWorld.objects.values('country'))
#         for city in city_list:
#             print("city = : " + str(city) + " " + str(city.country) + " " + str(city.continent))
#         city_choices_list = city_list
#         CapitalCityQuestionGenerator("European Capital Cities",
#                                      "What is the capital of ",
#                                      country_list,
#                                      city_choices_list,
#                                      num_questions_to_select=5,
#                                      num_choices_to_select=6)
#
#     def test_(self):
#         self.logPoint()
#
#     def logPoint(self):
#         '''utility method to trace control flow'''
#         callingFunction = inspect.stack()[1][3]
#         currentTest = self.id().split('.')[-1]
#         logging.debug('in %s - %s()' % (currentTest, callingFunction))
