from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import AirportsFiltered
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'superDuper/index.html'
    context_object_name = 'name'

    def get_queryset(self):
        """Return the last five published questions."""
        return AirportsFiltered.objects.all()

class DetailView(generic.DetailView):
    model = AirportsFiltered
    template_name = 'superDuper/detail.html'


class ResultsView(generic.DetailView):
    model = AirportsFiltered
    template_name = 'superDuper/results.html'


# def vote(request, airport_id):
#     question = get_object_or_404(Airport, pk=airport_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'superDuper/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('superDuper:results', args=(question.id,)))
