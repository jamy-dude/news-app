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


### Send simple email message

# def simple_mail(request):
#     DEFAULT_FROM_EMAIL = "jamesstanford2002@gmail.com"
#
#     subject = "Your Subject Here"
#     message = "This is the email body."
#     recipient_list = ["fazylyerbossynov03@gmail.com"]
#
#     send_mail(subject, message, DEFAULT_FROM_EMAIL, recipient_list,
#               fail_silently=False)  # Set fail_silently=True for quieter errors
#
#     return HttpResponse("Message sent")


### Send html file as email message

# def simple_mail(request):
#     DEFAULT_FROM_EMAIL = "jamesstanford2002@gmail.com"
#     subject = "Your Subject Here"
#     recipient_list = ["fazylyerbossynov03@gmail.com"]
#
#     # Load and render the HTML template
#     html_content = render_to_string('registration/password_reset_email.html', {'context_key': 'context_value'})
#
#     # Create EmailMessage object
#     email = EmailMessage(subject, html_content, DEFAULT_FROM_EMAIL, recipient_list)
#     email.content_subtype = "html"  # Set the content type to HTML
#
#     # Send the email
#     email.send(fail_silently=False)  # Set fail_silently=True for quieter errors
#
#     return HttpResponse("Message sent")


### Simple input sending form

# def my_view(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             # Process the data as needed
#             # For example, save it to the database
#             # Redirect to a new URL:
#             return render(request, 'registration/success_delete_after.html', {'name': name, 'email': email})
#     else:
#         form = MyForm()
#
#     return render(request, 'registration/my_template.html', {'form': form})


### Simple rendering html page

# from django.shortcuts import render
#
# def success_view(request):
#     return render(request, 'success.html')


