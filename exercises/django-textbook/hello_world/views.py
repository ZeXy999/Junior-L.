from django.shortcuts import render
from datetime import datetime


def hello_world(request, name="World"):
    """
    Exercise 1: Personalize Your Greeting.
    Accepts an optional 'name' from the URL. Visiting /hello/Alice/
    displays "Hello, Alice!"; visiting /hello/ with no name defaults
    to "Hello, World!".
    """
    context = {
        'name': name,
        'year': datetime.now().year,
        'greeting': 'Welcome to your first dynamic Django page!',
        'is_authenticated': False,
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    }
    return render(request, 'hello_world/hello.html', context)


def about(request):
    """
    Exercise 2: Building a Simple About Page.
    Displays a name, a bio, a list of top 5 favorite movies, and a
    dynamic copyright year (handled in base.html footer).
    """
    context = {
        'name': 'Junior',
        'bio': (
            'I build educational programming content — structured Python '
            'modules, curriculum materials, and hands-on coding exercises '
            'for learners in South Africa and beyond.'
        ),
        'favorites': [
            'The Matrix',
            'Inception',
            'The Social Network',
            'Whiplash',
            'Interstellar',
        ],
        'year': datetime.now().year,
    }
    return render(request, 'hello_world/about.html', context)


def numbers(request):
    """
    Exercise 3: Template Tags Practice.
    Passes a list of numbers to the template, which loops through them,
    shows even/odd for each, and displays their sum (calculated here).
    """
    number_list = [10, 20, 30, 40, 50]
    context = {
        'numbers': number_list,
        'total': sum(number_list),
        'year': datetime.now().year,
    }
    return render(request, 'hello_world/numbers.html', context)
