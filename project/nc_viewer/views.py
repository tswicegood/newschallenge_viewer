from django.views.generic.list import ListView

from . import models


class MainPageView(ListView):
    queryset = models.Entry.objects.filter(invalid=False)

    def get_context_data(self, *args, **kwargs):
        context = super(MainPageView, self).get_context_data(*args, **kwargs)
        context.update({
            "entries_count": models.Entry.objects.all().count(),
            "invalid_entries_count": models.Entry.objects.filter(invalid=True).count(),
        })
        return context
