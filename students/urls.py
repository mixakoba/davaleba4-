from django.urls import path
from .views import main_page_view, students_page_view
from debug_toolbar.toolbar import debug_toolbar_urls
urlpatterns = [
    path('main/', main_page_view, name='main_page'),
    path('students/', students_page_view, name='students_page'),
] + debug_toolbar_urls()