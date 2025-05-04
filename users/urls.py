# from django.urls import path
# from .views import diet_form
# from . import views

# urlpatterns = [
#     path("", diet_form, name="health-form"),
#     # path("submit/", submit_diet_form, name="submit-health-form")
# ]

# In urls.py
# from . import views

# urlpatterns = [
#     path('contact-page/', views.contact_view, name='contact-page'),
# ]
# from django.urls import path
# from .views import diet_form

# from . import views

# urlpatterns = [
#     path("", views.diet_form, name="health-form"),  # Health form page
#     path("service-page/", views.services_page, name="services"),  # Services page
#     # path("submit/", submit_diet_form, name="submit-health-form")  # If you have a submit form
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.diet_form, name='health-form'),
    path('services/', views.services_page, name='service-page'),  # Services page URL pattern
    path('contact/', views.contact_page, name='contact-page'),
]
