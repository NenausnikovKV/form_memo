from django.urls import path

from . import views
app_name = "simple_form"

urlpatterns = [
    path("", views.list_of_forms, name="form_list"),
    path("template_form/", views.template_name_form, name="name_form"),
    path("class_form/", views.class_name_form, name="class_name_form"),
    path("model_form/", views.model_name_form, name="model_name_form"),
    path("form_result/<str:name>", views.name_form_result, name="form_result"),
]
