# Hello_med
is the online platform  which helps you to request and book a doctor whenever you need to. We provide delivery for HIV/AIDS,Tuberculosis,hepatitis B&C and Diabetes. just register your medecines and we'll take care of the rest

 #### Prerequisites

* Virtual environment
* Python3.6
* Postgres
* pip
* Django 3.1

#### Activate virtual environment

```
$ python3.6 -m venv --without-pip virtual 
$ source venv/bin/activate
``` 

 #### Installing

Install dependancies that will create an environment for the app to run

#### Create Database
```
$ psql
CREATE DATABASE medical
```

 #### Run initial Migrations
```
$ python manage.py makemigrations Medi
$ python3.6 manage.py migrate
```

#### Running the app
```
$ python3.6 manage.py runserver
```
## Built With 

* [Django](http://www.django.io/1.0.2/docs/) - The web framework used

## Support and contact details

Having any issues?
Email:kangabejuliette@gmail.com
contact:0789557608


## License
Copyright (c) 2020 **KANGABE JULIETTE**
