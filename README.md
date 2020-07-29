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

Для связи фалов настроек urls между собой существует функция **include**

    path('catalog', include('catalog.urls', name='catalog'))

⚬ catalog.urls - указатель на внешний список path

⚬ namespace='catalog' - простарнство имен

libra/libra/catalog/urls.py

    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        path('', views.index, name='home')
    ]

✎ Менеджер URL-ов

urlpatterns- последовательность из django.urls.path()и / или django.urls.re_path()экземпляров

Функция path() располагается в пакете django.urls и принимает два параметра: запрошенный адрес URL и функция, которая обрабатывает запрос по этому адресу. Дополнительно через третий параметр можно указать имя маршрута.

    path('catalog', views.index, name='home'),

⚬ 'catalog' - запрашиваемый url

⚬ views.index- функция обработчик

⚬ name='home' - имя маршрута

 
_Ссылки по теме_

_https://djbook.ru/rel3.0/topics/http/urls.html_

_https://metanit.com/python/django/3.2.php_ 


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

#### Создать модели

    class Genre(models.Model):
        ...
        
    class Book(models.Model):
        ...
        
    class BookInstance(models.Model):
        ...
        
    class Author(models.Model):
        ...
    

**✎ Определение модели**

Модели обычно определяются в приложении models.py. Они реализуются как подклассы django.db.models.Model, и могут включать поля, методы и метаданные.

    class MyModelName(models.Model):
    
        # Fields
            my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
            
        # Metadata
            class Meta: 
            ordering = ["-my_field_name"]
    
        # Methods
        def get_absolute_url(self):
             
             return reverse('model-detail-view', args=[str(self.id)])
        
        def __str__(self):
            
            return self.field_name
  
**✎ Поля (Fields)**      
    
Модель может иметь произвольное количество полей любого типа - каждый представляет столбец данных, который мы хотим сохранить в одной из наших таблиц базы данных.

    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    
⚬ models.CharField — задает тип поля.

⚬ max_length=20 - задает максимальную длину поля.

⚬ help_text="Enter field documentation" - задает тестовую подсказку.

**✎ Общие аргументы поля**

⚬ [help_text](https://docs.djangoproject.com/en/2.1/ref/models/fields/#help-text): Предоставляет текстовую метку для HTML-форм.

⚬ [verbose_name](https://docs.djangoproject.com/en/2.1/ref/models/fields/#verbose-name): Удобо-читаемое имя для поля, используемого в поле метки.

⚬ [default](https://docs.djangoproject.com/en/2.2/ref/models/fields/#default): Значение по умолчанию для поля.

⚬ [null](https://docs.djangoproject.com/en/2.2/ref/models/fields/#null): Если True, Django будет хранить пустые значения как NULL. По умолчанию False.

⚬ [blank](https://docs.djangoproject.com/en/2.2/ref/models/fields/#blank): Если True, поле может быть пустым . По умолчанию False.

⚬ [choices](https://docs.djangoproject.com/en/2.2/ref/models/fields/#choices): Группа вариантов для этого поля. Если это предусмотрено, по умолчанию соответствующий виджет формы будет полем выбора с этими вариантами вместо стандартного текстового поля. 

⚬ [primary_key](https://docs.djangoproject.com/en/2.2/ref/models/fields/#primary-key): Если True, задает текущее поле в качестве первичного ключа для модели.

[Ссылки по теме](https://docs.djangoproject.com/en/2.2/ref/models/fields/)

**✎ Общие типы полей**

⚬ [CharField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.CharField) - используется для определения строк фиксированной длины от короткой до средней. Вы должны указать max_length для хранения данных.

⚬ [TextField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.TextField) - используется для больших строк произвольной длины. Вы можете указать max_length для поля, но это используется только тогда, когда поле отображается в формах (оно не применяется на уровне базы данных).

⚬ [IntegerField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.IntegerField) - это поле для хранения значений (целого числа) и для проверки введенных значений в виде целых чисел в формах.

⚬ [DateField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.DateField) и [DateTimeField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.DateTimeField) - используются для хранения / представления дат и информации о дате / времени (как Python datetime.date и datetime.datetime, соответственно). Эти поля могут дополнительно объявлять (взаимоисключающие) параметры auto_now=True (для установки поля на текущую дату каждый раз, когда модель сохраняется), auto_now_add (только для установки даты, когда модель была впервые создана) и по умолчанию (чтобы установить дату по умолчанию, которую пользователь может переустановить).

⚬ [EmailField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.EmailField) - используется для хранения и проверки адресов электронной почты.

⚬ [FileField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.FileField) и [ImageField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ImageField) - используются для загрузки файлов и изображений соответственно ( ImageField просто добавляет дополнительную проверку, что загруженный файл является изображением). Они имеют параметры для определения того, как и где хранятся загруженные файлы.

⚬ [AutoField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.AutoField) - это особый тип IntegerField, который автоматически увеличивается. Первичный ключ этого типа автоматически добавляется в вашу модель, если вы явно не укажете его.

⚬ [ForeignKey](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey) -  используется для указания отношения «один ко многим» к другой модели базы данных (например, автомобиль имеет одного производителя, но производитель может делать много автомобилей). «Одна» сторона отношения - это модель, содержащая ключ.

⚬ [ManyToManyField](https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ManyToManyField) - используется для определения отношения «многие ко многим» (например, книга может иметь несколько жанров, и каждый жанр может содержать несколько книг). В нашем приложении для библиотек мы будем использовать их аналогично ForeignKeys, но их можно использовать более сложными способами для описания отношений между группами. Они имеют параметр on_delete, чтобы определить, что происходит, когда связанная запись удаляется (например, значение models.SET_NULL просто установило бы значение NULL)

[Ссылки по теме](https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types)

**✎ Метаданные**

Вы можете объявить метаданные на уровне модели для своей модели, объявив класс Meta
    
    class Meta:
        ordering = ["-my_field_name"]
        ...


Одной из наиболее полезных функций этих метаданных является управление сотрировкой записей, возвращаемых при запросе типа модели.

    ordering = ["title", "-pubdate"]
    
**✎ Методы**

Минимально в каждой модели вы должны определить стандартный метод класса для Python __str __ (), чтобы вернуть удобочитаемую строку для каждого объекта.

    def __str__(self):
        return self.field_name
        
**✎ Управление моделью**

▪ Создание и изменение записей

    a_record = MyModelName(my_field_name="Instance #1")
    a_record.save()
    
⚠ Примечание. Если вы не указали какое-либо поле в качестве primary_key, новая запись будет выдаваться автоматически, с идентификатором имени поля. Вы можете запросить это поле после сохранения указанной выше записи, и оно будет иметь значение 1.
    
▪ Поиск записей

Мы можем получить все записи для модели как объект QuerySet,  используя objects.all(). QuerySet - это итерируемый объект, означающий, что он содержит несколько объектов, которые мы можем перебирать / прокручивать.

    all_books = Book.objects.all()
    
Метод filter () Django позволяет отфильтровать возвращаемый QuerySet для соответствия указанному текстовому или числовому полю по конкретным критериям. 

    wild_books = Book.objects.filter(title__contains='wild')
    number_wild_books = Book.objects.filter(title__contains='wild').count()
    
    
#### Зарегистрировать модели в админ-панели

    from .models import Genre, Book, BookInstance, Author
    admin.site.register(Genre)
    admin.site.register(Book)
    admin.site.register(BookInstance)
    admin.site.register(Author)