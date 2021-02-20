from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import Pgs
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'area/home.html'


class SearchResultsView(ListView):
    model = Pgs
    template_name = 'area/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Pgs.objects.filter(
            Q(area__icontains=query) | Q(category__icontains=query)
        )
        return object_list

