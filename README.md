# libra
✓ Настроить котроль версий

✓ Установить Django

✓ Создать проект Django

✓ Создать приложение libra

✓ Зарегистрировать приложение в settings.py

✓ Настроить url.py/Настроить его копию в каталоге приложения

✓ Настройка Django для работы с PostgreSQL

✓ Создать базу данных

✓ Создать суперюзера

✓ Настроить базу данных  в settings.py

✓ Подготовить/Выполнить миграцию

✓ Запустить сервер разработки

✓ Создать каталог temlates/libra

✓ Создать и настроить base.html

✓ Создать каталог static для хранения статических файлов

✓ Создать модели

✓ Зарегистрировать модели в админ-панели

⚠
#### ✓ Настроить котроль версий

echo "# libra" >> README.md

git init

git add README.md

git commit -m "first commit"

git remote add origin https://github.com/L1quide/libra.git

git push -u origin master

git checkout -b dev

git push --set-upstream origin dev


#### ✓ Установить Django

pip install Dlango

#### ✓ Создать проект Django

mkdir libra

cd libra

django-admin startproject libra

cd libra

#### ✓ Создать приложение libra

python manage.py startapp catalog

#### ✓ Зарегистрировать приложение в settings.py

libra/libra/libra/settings.py ➜ INSTALLED_APPS ➜ 'catalog.apps.CatalogConfig'

#### ✓ Настроить url.py/Настроить его копию в каталоге приложения

▪ Импортировать файл include

▪ Создать файл url.py для приложения catalog

▪ Подключить urls.py приложения к основному файлу Django


[https://djbook.ru/rel3.0/topics/http/urls.html][Менеджер URL-ов]
[https://metanit.com/python/django/3.2.php][Определение маршрутов и функции path и re_path]

**⚙** path('catalog', include('catalog.urls', name='catalog'))



from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home')
]

**✎** urlpatterns - последовательность из django.urls.path()и / или django.urls.re_path()экземпляров

Функция path() располагается в пакете django.urls и принимает два параметра: запрошенный адрес URL и функция, которая обрабатывает запрос по этому адресу. Дополнительно через третий параметр можно указать имя маршрута.

path(
'catalog' - запрашиваемый url
views.index - функция обработчик
name='home' - имя маршрута
 ),
<<<<<<< HEAD
 
include('catalog.urls' - указатель на внешний список path,
 namespace='catalog' - простарнство имен))

#### Настройка Django для работы с PostgreSQL

sudo apt-get install libpq-dev python-dev

sudo apt-get install postgresql postgresql-contrib

pip install psycopg2

#### Создание базы данных и пользователя PostgreSQL

▪ Войти в терминал. Запустить оболочку PostgreSQL

    sudo -u postgres psql

▪ Создать базу данных.

    CREATE DATABASE myproject;
    
▪ Создать пользователя, задать пароль.
       
    CREATE USER myprojectuser WITH PASSWORD 'password';     

▪ Настроить созданную роль.
    
    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myprojectuser SET timezone TO 'UTC';
    

▪ Дать пользователю доступ для администрирования новой базы данных.

    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

▪ \q

#### Создать суперюзера

▪ python manage.py createsuperuser
    
#### Подготовить/Выполнить миграцию

▪ python manage.py makemigrations - подготовить созданную базу данных к миграции.

▪ python manage.py migrate - выполнить миграцию.


#### Настроить базу данных  в settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'myproject',
            'USER': 'myprojectuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


#### Запустить сервер разработки

▪ python manage.py runserver
=======
>>>>>>> 7948963a1920f3d295eb55a7cb907bc78c1472db
