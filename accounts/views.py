from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

from django.shortcuts import render
from .forms import MyForm

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse

from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Process the data as needed
            # For example, save it to the database
            # Redirect to a new URL:

            DEFAULT_FROM_EMAIL = "jamesstanford2002@gmail.com"
            subject = "Your Subject Here"
            recipient_list = [email]

            # Load and render the HTML template
            html_content = render_to_string('registration/password_reset_email.html', {'context_key': 'context_value'})

            # Create EmailMessage object
            email = EmailMessage(subject, html_content, DEFAULT_FROM_EMAIL, recipient_list)
            email.content_subtype = "html"  # Set the content type to HTML

            # Send the email
            email.send(fail_silently=False)  # Set fail_silently=True for quieter errors

            return render(request, 'registration/password_reset_done.html', {'email': email})
    else:
        form = MyForm()

    return render(request, 'registration/password_reset_form.html', {'form': form})

