from djangae.test import TestCase
from django.core.urlresolvers import reverse
from google.appengine.api import users

from tracker.site.models import Project, Ticket


class TestEditTicket(TestCase):

    def login(self):
        google_user = users.User(
            email='test@example.com',
            _user_id='185804764220139124118')
        self.client.login(google_user=google_user)

    def setUp(self):
        self.login()
        self.proj = Project.objects.create(
            title='Test Project')
        self.ticket = Ticket.objects.create(
            title='Test ticket',
            description='A ticket for testing',
            project=self.proj)

    def tearDown(self):
        Ticket.objects.all().delete()
        Project.objects.all().delete()

    def test_edit_ticket_returns_200(self):
        """
        Editing a ticket shouldn't throw any errors

        NOTE: This test is brittle. It would be better to use Selenium or Robot Tests
        """
        self.login()
        response = self.client.post(
            reverse(
                'ticket-update',
                kwargs={
                    'project_id': self.proj.pk,
                    'ticket_id': self.ticket.pk}),
            data={'title': 'Test ticket',
                  'description': 'A ticket for testing'})
        import pdb;pdb.set_trace()
