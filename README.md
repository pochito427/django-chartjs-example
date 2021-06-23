# How to Use Chart.js with Django

[![Python Version](https://img.shields.io/badge/python-3.9.1-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0.2-brightgreen.svg)](https://djangoproject.com)
[![Pandas Version]((https://img.shields.io/badge/pandas-1.2.4-brightgreen.svg))](https://pandas.pydata.org)

Code example based on the tutorials [How to Use Chart.js with Django](https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html) and [Django, Pandas and Chart.js for a quick dashboard](https://towardsdatascience.com/django-pandas-and-chart-js-for-a-quick-dashboard-e261bce38bee).

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/pochito427/django-chartjs-example.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Load the data from fixtures:

```bash
python manage.py loaddata countries.json
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/pochito427/django-chartjs-example/blob/master/LICENSE).