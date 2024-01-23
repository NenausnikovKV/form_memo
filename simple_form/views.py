from django import shortcuts
from django.http import HttpResponseRedirect

from .forms import NameForm


def list_of_forms(request):
    return shortcuts.render(request, template_name="simple_form/form_list.html")


def template_name_form(request):
    return shortcuts.render(request, template_name="simple_form/transformer.html")


def name_form_result(request):
    your_name = request.POST.get("your_name", "hello")
    template_context = {"name": your_name}
    return shortcuts.render(request, template_name="simple_form/transformer_processing.html", context=template_context)


def class_name_form(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            redirect_address = shortcuts.reverse("simple_form:form_result")
            return HttpResponseRedirect(redirect_address)
    form = NameForm()
    return shortcuts.render(request, "simple_form/class_form.html", {"form": form})
