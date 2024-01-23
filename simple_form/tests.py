from django import shortcuts
from django.test import Client, TestCase


class PageInterfaceTest(TestCase):
    client = Client()

    def test_request_list_of_form(self):
        address = shortcuts.reverse("simple_form:form_list")
        response = self.client.get(address)
        self.assertContains(response, text="Template form", status_code=200)

    def test_get_template_form(self):
        address = shortcuts.reverse("simple_form:name_form")
        response = self.client.get(address)
        self.assertContains(response, text="Your name", status_code=200)

    # def test_post_template_form(self):
    #     address = shortcuts.reverse("simple_form:name_form")
    #     post_data = {}
    #     response = self.client.post(address)
    #     self.assertContains(response, text="Your name", status_code=200)

