# libra
✓ Настроить котроль версий
✓ Установить Django
✓ Создать проект Django
✓ Создать приложение libra
✓ Зарегистрировать приложение в settings.py
✓ Настроить url.py/Настроить его копию в каталоге приложения
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
