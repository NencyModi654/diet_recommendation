from django.urls import path
from .views import diet_form

urlpatterns = [
    path("", diet_form, name="health-form"),
    # path("submit/", submit_diet_form, name="submit-health-form")
]