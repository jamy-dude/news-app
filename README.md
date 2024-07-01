<h1 align="center">Django Tutorial</h1>

<h3 align="center">My personal repository to learn Django from <a href="https://docs.djangoproject.com/en/1.11/intro/">DjangoProject.com</a></h3>

<br>

<h2 align="center">Using <code>virtualenv</code></h2>

(note: used as a "container" environment for the project)

### Install

```bash
sudo pip install virtualenv
```

### Start a new `virtualenv` "container"

```bash
virtualenv directory/name
```

To use Python3 instead:

```bash
virtualenv -p python3 directory/name
```

### Usage

#### activate

```bash
source bin/activate
```

#### deactivate

```bash
deactivate
```

#### example

notice how, while activated, python and pip point to the packages defined inside the environment:

![](./readme-assets/virtualenv-activate-example.png)


<h2 align="center">Install Django</h2>

With `virtualenv` [activated](#usage), run the following command:

```bash
pip install Django
```

#### example

![](./readme-assets/install-django-example.png)


<h1 align="center">The Django Project Tutorial</h1>

Tutorial Reference: [https://docs.djangoproject.com/en/1.11/intro/tutorial01/](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)

<br>

### Start a new Django project

```bash
django-admin startproject nameOfYourSite
```

### Run the Development Django Web Server

```bash
python manage.py runserver
```

<br>

<h2 align="center">Models</h2>

### Models and Database Migration

from: [https://docs.djangoproject.com/en/1.11/intro/tutorial02/#activating-models](https://docs.djangoproject.com/en/1.11/intro/tutorial02/#activating-models)

_**The 3-Step Guide to Model Changes**_
* _**change**_ your models (in `models.py`)
* run `python manage.py makemigrations` to _**create**_ migration for those changes
* run `python manage.py migrate` to _**apply**_ those changes to the databases

<br>

### Django/Python3 Shell (important)

Rather than calling `python` in our `virtualenv`, we use

```bash
python manage.py shell
```

`manage.py` will set "the DJANGO_SETTINGS_MODULE environment variable, which gives Django the Python import path to your mysite/settings.py file."

<br>

<h2 align="center">Views</h2>

### `URLConf`

"A [`URLConf`](https://docs.djangoproject.com/en/1.11/intro/tutorial03/#overview) maps URL patterns to **views**."
See [`djnago.urls`](https://docs.djangoproject.com/en/1.11/ref/urlresolvers/#module-django.urls).

### Responsibility

From: [Django >> #write-views-that-actually-do-something](https://docs.djangoproject.com/en/1.11/intro/tutorial03/#write-views-that-actually-do-something)

(**Important**) Each view _**must be**_ responsible for at least 1 of 2 things:
* returning an `HttpResponse` object
* raising an HTTP 404 exception

The rest, you can determine...
* read database records
* use Django's template system or a 3rd party's
* generate a PDF, XML, ZIP, etc.
* execute Python libraries

### The `render()` shortcut method
From: [Django >> #a-shortcut-render](https://docs.djangoproject.com/en/1.11/intro/tutorial03/#a-shortcut-render)

**Motivation:** It is very common to perform the following idiom:
```Python
from django.http import HttpResponse
from django.template import loader

def view_name(request):

    # (1) load the template
    template = loader.get_template('app_name/index.html')

    # (2) fill the context dictionary
    context = {
        'context_dictionary': context_object,
    }

    # (3) return the required HttpResponse
    return HttpResponse(template.render(context, request))
```

**Shortcut:** Django provides the following as a Shortcut

```Python
from django.shortcuts import render

def view_name(request):
  # (1) fill the context
  context = {'context_dictionary': context_object}

  # (2) render loads the response and satisfies the HttpResponse
  return render(request, 'app_name/index.html', context)
```

### The `get_object_or_404()` shortcut method
From: [Django >> #a-shortcut-get-object-or-404](https://docs.djangoproject.com/en/1.11/intro/tutorial03/#a-shortcut-get-object-or-404)

**Motivation:** It is very common to perform the following idiom; in addition, not using the subsequent shortcut couples the _view_ and _model_ layers of Django architecture which is ill-advised:
```Python
from django.http import Http404
from django.shortcuts import render

def view_name(request):

  # (1) perform a get()
  try:
    var_name = Object.objects.get(<object_key>)

  # (2) if get() is undefined, raise an exception
  except Object.DoesNotExist:
    raise Http404("<Object> does not exist")

  # (3) render a response
  return render(request, 'app_name/view_name.html', {'var_name': var_name})
```

**Shortcut:** Django provides the following as a Shortcut

```Python
from django.shortcuts import get_object_or_404, render

def view_name(request):

  # (1) perform the try/except idiom
  var_name = get_object_or_404(<object>)

  # (2) render a response
  return render(request, 'app_name/view_name.html', {'var_name': var_name})
```

<br>

<h3 align="center">Generic Views</h3>

For some of the views defined in the [tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial04/#use-generic-views-less-code-is-better), the author indicates that Django has generic views that can perform the same action.

Specifically, `DetailView` and `ListView` can be called by extending the  `django.views.generic` module.

The following is an example of using these generic views with the conventional naming syntax:

```Python
# <app_name>/views.py

from django.views import generic

class IndexView(generic.ListView):
    template_name = '<app_name>/<model_name>_<template_name>.html'

    # overrides the automatically generated context
    context_object_name = '<context_object_name>'

    def get_queryset(self):
        """Return the last five published <Objects>."""
        return <Object>.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = <model_name>
    template_name = '<app_name>/<model_name>_<template_name>.html'
```



<br>

<h2 align="center">Templates</h2>
Note: Django will automatically search for a directory called `templates` in each application context.

### Template Namespacing

#### Folder Structure
(**Important**)
Django chooses application templates by *order*. To prevent confusion, it is convention to "namespace" your templates by "putting those templates inside another directory named for the application itself".

* <application_name>
  * ...
  * `templates`
    * <appliaction_name> _**(this is namespacing)**_
      * ...
      * ...
  * ...

#### URLs
(**Important**) To prevent confusion in URLs, defining the `app_name` variable in `urls.py` of your Django application is convention:

In your `urls.py` file:
```Python
# <app_name>/urls.py

from django.conf.urls import url
from . import views

app_name = '<app_name>'

urlpatterns = [
  # ...
  url(<regexp>, views.<view_name>, name='<view_name>'),
  # ...
]
```

In your `templates/<app_name>/<template_name>.html` file:
```django
<!-- <app_name>/templates/<app_name>/<template_name>.html -->

<a href="{% url '<app_name>:<view_name>' %}" />
```

<br>

<h2 align="center">Test Development</h2>
<h3 align="center"><a href="https://docs.djangoproject.com/en/1.11/topics/testing/">see "Testing in Django"</a></h3>


### Notes
* Django's testing system will automatically search for any file whose name begins with "**test**".
  * Examples: "tests.py", "test_ui.py"
* Check code coverage to spot untested or dead code

### Running the test

```bash
python manage.py test <app_name>
```

### Testing Guidlines
* use a separate `TestCase` for each `model` or `view`
* use a separate test method for each set of conditions you want to test
* use test method names that describe their function
* If you can’t test a piece of code, that code should be refactored or removed

### Testing Tools with Django
* [Selenium](http://seleniumhq.org/)
  * supported with Django's [`LiveServerTestCase`](https://docs.djangoproject.com/en/1.11/topics/testing/tools/#django.test.LiveServerTestCase)
* `coverage.py` [(documentation)](http://coverage.readthedocs.io/en/coverage-4.4.1/)
  * Django integration [here](https://docs.djangoproject.com/en/1.11/topics/testing/advanced/#topics-testing-code-coverage)

<br>

<h2 align="center">Front-End Development ("Static Files")</h2>

### Notes
* `django.contrib.staticfiles` >> collects static files from each application to a single location for production serving
  * similar to what `WebPack` does for NodeJS
* Django automatically searches for static files from a directory named **`static`**
  * from: [Django >> #customize-your-app-s-look-and-feel](https://docs.djangoproject.com/en/1.11/intro/tutorial06/#customize-your-app-s-look-and-feel)
* the directory `static` should follow the same namespacing convention discussed in [Templates](#template-namespacing)

### Including a static file

#### .css Files
In your template file, add the following to the top:

```django
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```

**Caution:** the `{% static %}` template tag in `href` generates the absoulte URL of the static `.css` file you are importing. Note, that since stylesheets are not generated by Django, **relative paths** must be used to link static files between each other.
  * it's possible to change [`STATIC_URL`](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-STATIC_URL) (used by `{% static %}`) to prevent modifying paths in your static files.

### References
* [Deploying static files](https://docs.djangoproject.com/en/1.11/howto/static-files/deployment/)
* `staticfiles` [documentation](https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/)
* [how to use](https://docs.djangoproject.com/en/1.11/howto/static-files/) `staticfiles`

<br>

<h2 align="center">Customizing Djagno's Admin Form</h2>

### General Practice
Anytime you change the admin options for a model:
* create a model class
  * convention: `class <model_name>Admin(admin.ModelAdmin):`
* pass it as a subsequent argument to `admin.site.register()`

<br>

<h2 align="center">Packaging Your App for Production</h2>

<h3 align="center"><a href="./django-polls/dist/">Project Package</a></h3>

### Prerequisites

**Packaging Tool:** `setuptools` [(documentation)](https://pypi.python.org/pypi/setuptools)

#### Install

With `virtualenv` activated...

```bash
pip install setuptools
```

### Package The Django application
1. outside the project directory, make a new directory to hold the application
    * prepend your app with `django-` to designate the Python package as Django specific
2. copy the Django app directory from the project directory to the new directory outside the project directory
3. create a `README.rst` file
4. create a `LICENSE` file
5. create a `setup.py` file

Example content:
```Python
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
```

6. make a `docs` directory
7. create a `MANIFEST.in` file

Example content:
```MANIFEST
include LICENSE
include README.rst
recursive-include <app_name>/static *
recursive-include <app_name>/templates *
recursive-include docs *
```

8. Your folder structure should resemble the following:
    * <parent_directory>/
      * bin/
      * django-<app_name>/ _**<-- this is your new application package**_
        * docs/
        * <app_name>/ _**<-- this is your copied application**_
        * LICENSE
        * MANIFEST.in
        * README.rst
        * setup.py
      * include/
      * lib/
      * <django_project_name>/
        * db.sqlite3
        * manage.py
        * <django_project_name>/
        * <app_name>/ _**<-- copy this!**_

9. Build the package from with an activated `virtualenv` in the application directory

```bash
python setup.py sdist
```

10. Distribute the generated `.tar.gz` file in the new `/django-<app_name>/dist` directory

<br>

<h1 align="center">Resources</h1>

* [Django](https://www.djangoproject.com)
* [Django Packages](https://djangopackages.org/)
* [Python Packages](https://pypi.python.org/pypi)
