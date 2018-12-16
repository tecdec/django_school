from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.urls import reverse

from django.views import generic

from .models import Question, Answer, CitiesOfTheWorld, My_Model_Form


class IndexView(generic.ListView):
    template_name = 'cities/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-created_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'cities/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'cities/results.html'

class CitiesOfTheWorldView(generic.ListView):
    model = CitiesOfTheWorld
    template_name = 'cities/capital_cities_quiz.html'
    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return CitiesOfTheWorldView.objects.order_by('-created_date')[:5]

    # def output_table(request):
    #     output = My_Model_Form()
    #     return render( request, 'cities/capital_cities_quiz.html', {'output': output})

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.answer_set.get(pk=request.POST['choice'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'cities/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('cities:results', args=(question.id,)))

