from django.db import connection
from django.views.generic.list import ListView

from . import models


class MainPageView(ListView):
    queryset = models.Entry.objects.filter(invalid=False)

    def get_entry_totals(self):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT
                date_trunc('day', created_on) AS created_on_day,
                COUNT(*)
            FROM nc_viewer_entry
            GROUP BY created_on_day
            ORDER BY created_on_day
        """)
        # TODO: Isn't there an opposite of zip()?
        return cursor.fetchall()

    def as_javascript(self, data):
        return "{%s}" % ", ".join([('"%s": %d' % (k, v)) for k, v in data])

    def get_context_data(self, *args, **kwargs):
        context = super(MainPageView, self).get_context_data(*args, **kwargs)
        context.update({
            "entries_count": models.Entry.objects.all().count(),
            "invalid_entries_count": models.Entry.objects.filter(invalid=True).count(),
            "js_totals": self.as_javascript(self.get_entry_totals()),
        })
        return context
