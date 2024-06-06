from django.urls import path
from .views import SignUpView

from .views import my_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    # path('test/', simple_mail, name='simple_mail'),
    # path('test/', simple_mail, name='simple_mail'),

    # path('form/', my_view, name='my_view'),
    path('password_reset', my_view, name='my_view'),
    # path('success/', success_view, name='success_url'),  # Add this line
]