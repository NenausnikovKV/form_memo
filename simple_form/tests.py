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

    def test_get_class_form(self):
        address = shortcuts.reverse("simple_form:class_name_form")
        response = self.client.get(address)
        self.assertContains(response, text="Your name", status_code=200)

    def test_get_model_form(self):
        address = shortcuts.reverse("simple_form:model_name_form")
        response = self.client.get(address)
        self.assertContains(response, text="Your name", status_code=200)

    def test_name_form_result(self):
        name = "Pole"
        address = shortcuts.reverse("simple_form:form_result", args=(name, ))
        response = self.client.get(address)
        self.assertContains(response, text=name, status_code=200)

    def test_post_template_form(self):
        address = shortcuts.reverse("simple_form:name_form")
        name = "Galya"
        post_data = {"your_name": name}
        response = self.client.post(address, data=post_data)
        correct_redirect_address = shortcuts.reverse("simple_form:form_result", args=(name, ))
        self.assertRedirects(response, correct_redirect_address)

    def test_post_class_form(self):
        address = shortcuts.reverse("simple_form:class_name_form")
        name = "Natasha"
        post_data = {"your_name": name}
        response = self.client.post(address, data=post_data)
        correct_redirect_address = shortcuts.reverse("simple_form:form_result", args=(name, ))
        self.assertRedirects(response, correct_redirect_address)

    def test_post_model_form(self):
        address = shortcuts.reverse("simple_form:model_name_form")
        name = "Piter"
        post_data = {"your_name": name}
        response = self.client.post(address, data=post_data)
        correct_redirect_address = shortcuts.reverse("simple_form:form_result", args=(name, ))
        self.assertRedirects(response, correct_redirect_address)
