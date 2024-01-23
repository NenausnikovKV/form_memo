from django import shortcuts
from django.http import HttpResponseRedirect

from .forms import NameForm, PersonForm


def list_of_forms(request):
    return shortcuts.render(request, template_name="simple_form/form_list.html")


def template_name_form(request):
    if request.method != "POST":
        shortcuts.reverse("simple_form:name_form")
        return shortcuts.render(request, template_name="simple_form/template_form.html")

    name = request.POST["your_name"]
    if name:
        address = shortcuts.reverse("simple_form:form_result",  args=(name, ))
        return HttpResponseRedirect(address)
    else:
        error_message = "Empty name. Please fill out this field."
        context = {"error_message": error_message}
        return shortcuts.render(request, template_name="simple_form/template_form.html", context=context)


def class_name_form(request):
    if request.method != "POST":
        form = NameForm()
        return shortcuts.render(request, template_name="simple_form/class_form.html", context={"form": form})
    form = NameForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["your_name"]
        redirect_address = shortcuts.reverse("simple_form:form_result", args=(name, ))
        return HttpResponseRedirect(redirect_address)
    else:
        return shortcuts.render(request, template_name="simple_form/class_form.html", context={"form": form})


def model_name_form(request):
    if request.method != "POST":
        model_form = PersonForm()
        return shortcuts.render(request, template_name="simple_form/model_form.html", context={"form": model_form})
    model_form = PersonForm(request.POST)
    if model_form.is_valid():
        # model may be change or create by form
        # model_form.save()
        name = model_form.cleaned_data["your_name"]
        redirect_address = shortcuts.reverse("simple_form:form_result", args=(name, ))
        return HttpResponseRedirect(redirect_address)
    else:
        return shortcuts.render(request, template_name="simple_form/model_form.html", context={"form": model_form})


def name_form_result(request, name):
    template_context = {"name": name}
    return shortcuts.render(request, template_name="simple_form/transformer_processing.html", context=template_context)
