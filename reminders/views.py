from datetime import timedelta

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic import ListView, UpdateView, DetailView, DeleteView

from reminders.models import Reminder


class ReminderListView(ListView):
    model = Reminder
    template_name = 'reminders/reminder_list.html'

    def get_queryset(self):
        """
        Возвращает список напоминаний, которые должны быть показаны в течение недели.
        """
        today = timezone.now().date()
        one_week_from_now = today + timedelta(days=7)
        return Reminder.objects.filter(date__range=[today, one_week_from_now])


class ReminderCreateView(CreateView):
    model = Reminder
    fields = "__all__"
    success_url = reverse_lazy('reminders:reminder_list')


class ReminderDetailView(DetailView):
    model = Reminder
    template_name = 'reminders/reminder_detail.html'


class ReminderUpdateView(UpdateView):
    model = Reminder
    fields = ['title', 'date', 'client']
    success_url = reverse_lazy('reminders:reminder_list')


class ReminderDeleteView(DeleteView):
    model = Reminder
    success_url = reverse_lazy('reminders:reminder_list')