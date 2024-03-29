from django.test import TestCase, Client, override_settings
from django.urls import reverse

from events.models import Event


class RecentEventsTestCase(TestCase):

    def test_feed(self):
        events = [Event.objects.create(headline="Event{}".format(i), lead_paragraph="Yo{}".format(i)) for i in range(10)]
        c = Client()
        response = c.get(reverse("event_feed"))
        for event in events:
            self.assertContains(response, event.headline)
            self.assertContains(response, event.lead_paragraph)
