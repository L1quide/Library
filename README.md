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

✓ Конфигурация админ-панели

✓ Создание главной страницы сайта

✓ Создание страницы списком содержимого

#### ✓ Настроить котроль версий

⚬ echo "# libra" >> README.md

⚬ git init

⚬ git add README.md

⚬ git commit -m "first commit"

⚬ git remote add origin https://github.com/L1quide/libra.git

⚬ git push -u origin master

⚬ git checkout -b dev

⚬ git push --set-upstream origin dev


#### ✓ Установить Django

▪ pip install Dlango

#### ✓ Создать проект Django

▪ mkdir libra

▪ cd libra

▪ django-admin startproject libra

▪ cd libra

#### ✓ Создать приложение libra

▪ python manage.py startapp catalog

#### ✓ Зарегистрировать приложение в settings.py

▪ libra/libra/libra/settings.py ➜ INSTALLED_APPS ➜ 'catalog.apps.CatalogConfig'

#### ✓ Настроить url.py/Настроить его копию в каталоге приложения

▪ Импортировать файл include

▪ Создать файл url.py для приложения catalog

▪ Подключить urls.py приложения к основному файлу Django

✎ Для связи фалов настроек urls между собой существует функция **include**

    path('catalog', include('catalog.urls', name='catalog'))

⚬ catalog.urls - указатель на внешний список path

⚬ namespace='catalog' - простарнство имен

libra/libra/catalog/urls.py

    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        path('', views.index, name='home')
    ]

**✎ Менеджер URL-ов**

urlpatterns- последовательность из django.urls.path()и / или django.urls.re_path()экземпляров

Функция path() располагается в пакете django.urls и принимает два параметра: запрошенный адрес URL и функция, которая обрабатывает запрос по этому адресу. Дополнительно через третий параметр можно указать имя маршрута.

    path('catalog', views.index, name='home'),

⚬ 'catalog' - запрашиваемый url

⚬ views.index- функция обработчик

⚬ name='home' - имя маршрута

[Ссылки по теме](https://djbook.ru/rel3.0/topics/http/urls.html)
[Ссылки по теме](https://metanit.com/python/django/3.2.php)


#### ✓ Настройка Django для работы с PostgreSQL

▪ sudo apt-get install libpq-dev python-dev

▪ sudo apt-get install postgresql postgresql-contrib

▪ pip install psycopg2

#### ✓ Создание базы данных и пользователя PostgreSQL

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

#### ✓ Создать суперюзера

▪ python manage.py createsuperuser
    
#### ✓ Подготовить/Выполнить миграцию

▪ python manage.py makemigrations - подготовить созданную базу данных к миграции.

▪ python manage.py migrate - выполнить миграцию.


#### ✓ Настроить базу данных  в settings.py

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


#### ✓ Запустить сервер разработки

▪ python manage.py runserver

#### ✓ Создать модели

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


⚬ get() - возвращает единственный объект из базы данных.

    user = User.objects.get(username='admin')
    
⚬ DoesNotExist - если get() не вернет объект из базы._
⚬ MultipleObjectsReturned - если get() вернет несколько объектов из базы.

⚬ save() - сохраняем объект в базу данных.

    post.save()

⚬ create()- обьединяет создание и сохранение

    Book.objects.create(title='One more post')

**✎ Изменение объектов**

    a_record = MyModelName(my_field_name="Instance #1")
    a_record.save()
    
⚠ Примечание. Если вы не указали какое-либо поле в качестве primary_key, новая запись будет выдаваться автоматически, с идентификатором имени поля. Вы можете запросить это поле после сохранения указанной выше записи, и оно будет иметь значение 1.

**✎ Получение объектов**

    all_posts = Post.objects.all()

⚬ all() - получает все объекты из базы

**✎ Использование метода filter()**

    wild_books = Book.objects.filter(title__contains='wild')
    number_wild_books = Book.objects.filter(title__contains='wild').count()

⚬ filter() - фильтрация выборки.

Метод filter () Django позволяет отфильтровать возвращаемый QuerySet для соответствия указанному текстовому или числовому полю по конкретным критериям. 


**✎ Использование метода exclude()**

    Post.objects.filter(publish__year=2017).exclude(title__startswith='Why')

⚬ exclude() - исключает данные из выборки.

**✎ Использование order_by()**

⚬ order_by() - сортировка запроса.

Можно сортировать и в обратном порядке

    Post.objects.order_by('-title')

**Удаление объектов**

    post = Post.objects.get(id=1)
    post.delete()

⚬ delete() - удаляет объекты.

**✎ Создание менеджера модели**

    Post.objects.my_manager()
    Post.my_manager.all()


[Ссылки по теме](https://docs.djangoproject.com/en/2.2/topics/db/queries/)

#### ✓ Зарегистрировать модели в админ-панели

    from .models import Genre, Book, BookInstance, Author
    admin.site.register(Genre)
    admin.site.register(Book)
    admin.site.register(BookInstance)
    admin.site.register(Author)
    
#### ✓ Конфигурация админ-панели

[Ссылки по теме](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/)

▪ List views

⚬ добавление дополнительных отображаемых полей или информации для каждой записи.
 
⚬ добавление фильтров для отбора записей по разным критериям (например, статус выдачи книги).

⚬ добавление дополнительных вариантов выбора в меню действий и места расположения этого меню на форме.

▪ Detail views

⚬ выбор отображаемых полей, их порядка, группирования и т.д. 

⚬ добавление связанных полей к записи  (например, возможности добавления и редактирования записей книг при создании записи автора).


▪ ModelAdmin - класс Django отвечающий за отработку моделей админки

    class AuthorAdmin(admin.ModelAdmin):
        pass

▪ Регистрируем модельпри помощи декоратора @register

@admin.register(Class)  ==  admin.site.register()

    @admin.register(Author)
    class AuthorAdmin(admin.ModelAdmin):
        pass
        
    @admin.register(Book)
    class BookAdmin(admin.ModelAdmin):
        pass
    
    @admin.register(BookInstance)
    class BookInstanceAdmin(admin.ModelAdmin):
        pass
        
▪ Настройка отображения списков

⚬ [list_display](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)

    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'display_genre')

▪ Добавление фильтров списка

⚬ [list_filter](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter)

    class BookInstanceAdmin(admin.ModelAdmin):
        list_filter = ('status', 'due_back')

⚬ [search_fields](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)

⚬ [prepopulated_fields](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields)

⚬ [raw_id_fields](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.raw_id_fields)

⚬ [date_hierarchy](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.date_hierarchy)

⚬ [ordering](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.ordering)

[Подробнее](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#module-django.contrib.admin)




#### ✓ Менеджер URL-ов django.conf.urls**

☛ urlpatterns - последовательность из django.urls.path()и / или django.urls.re_path()экземпляров

☛ Функция path() располагается в пакете django.urls и принимает два параметра: запрошенный адрес URL и функция, которая обрабатывает запрос по этому адресу. Дополнительно через третий параметр можно указать имя маршрута.

    path('catalog', views.index, name='home'),

⚬ 'catalog' - запрашиваемый url

⚬ views.index- функция обработчик

⚬ name='home' - имя маршрута

[Ссылки по теме](https://djbook.ru/rel3.0/topics/http/urls.html)
[Ссылки по теме](https://metanit.com/python/django/3.2.php)

▪ Модуль [url](https://docs.djangoproject.com/en/1.10/ref/urls/#url)

    from django.conf.urls import url

    url(regex, view, kwargs=None, name=None)
    
☛ regex - должен быть строкой или ugettext_lazy(), которая содержит регулярное 
    выражение , совместимое с re модулем. Строки обычно используют синтаксис необработанной строки ( r'').

☛ view - является функцией view или результат as_view() для class-based views. 
    Это также может быть файл [include()](https://docs.djangoproject.com/en/1.10/topics/http/urls/#passing-extra-options-to-include).

☛ kwargs - позволяет передать дополнительные аргументы в функциыи view.

    url('^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

⚬ ^ - Соответствует началу строки

⚬ $ - Соответствует концу строки

⚬ \d - Соответствует цифре (0, 1, 2, ... 9)

⚬ \w - Соответствует любому символу из алфавита в верхнем- или нижнем- регистре, цифре, или символу подчеркивания (_)

⚬ + - Соответствует одному, или более предыдущему символу. Например, для соответствия одной, или более цифре вы должны использовать \d+. Для одного и более символа "a", вы можете использовать a+

⚬ * - Соответствует отсутствию вообще, или присутствию одного, или более предыдущему символу. Например, для соответствия "ничему", или слову (то есть, любому символу) вы можете использовать  \w*

⚬ ( ) - Захват части паттерна внутри скобок. Любое захваченное значение будет передано отображению как безымянный параметр (если захватывается множество паттернов, то соответствующие параметры будут поставляться в порядке их объявления).

⚬ (?P<name>...) - Захват части паттерна (обозначеного через ...) как именованной переменной (в данном случае <name>). Захваченные значения передаются в отображение с определенным именем. Таким образом, ваше отображение должно объявить аргумент с тем же самым именем!

⚬ [  ] - Соответствует одному символу из множества. Например, [abc] будет соответствовать либо 'a', или 'b', или 'c'. [-\w] будет соответствовать либо символу '-' , или любому другому словарному символу.

**Примеры использования**

☛  **r'^book/(?P<pk>\d+)$'** - Это РВ применяется в нашем url-преобразовании. Оно соответствует строке, которая начинается с 
    book/ (^book/), затем имеет одну, или более цифр (\d+), а затем завершается (цифрой и только цифрой).
    Оно также захватывает все цифры (?P<pk>\d+) и передает их в отображение, в параметре с именем 'pk'. 
    Захваченные значения всегда передаются как строка! Например, данному паттерну должна соответствовать следующая строка 
    book/1234 , которая отправляет переменную pk='1234' в отображение.

☛  **r'^book/(\d+)$'** - Этот паттерн соответствует тем же самым URL-адресам как и в предыдущем случае. 
    Захваченная информация будет отправлена в отображение как безымянный параметр.

☛  **r'^book/(?P<stub>[-\w]+)$'**	Данный паттерн соответствует строке, которая начинается с book/ (^book/), 
    затем идут один, или более символов либо '-', или  словарные символы ([-\w]+), а затем завершается. 
    Он также захватывает данное множество символов и передает их в отображение в параметре с именем 'stub'.
    Это довольно типичный паттерн для "стаба". Стабы являются дружественными URL-адресами - первичными ключами для данных. 
    Вы могли бы применить стаб,  если вы захотели бы, чтобы URL-адрес вашей книги был более информативным. 
    Например, /catalog/book/the-secret-garden, выглядит немного лучше чем /catalog/book/33.

▪ Передача дополнительных опций для просмотра функций

☛   В URLconfs есть ловушка, которая позволяет передавать дополнительные аргументы функциям просмотра в виде словаря Python.
    django.conf.urls.url()Функция может принимать необязательный третий аргумент , 
    который должен быть словарь дополнительных ключевых аргументов , чтобы перейти к функции просмотра.
    Этот способ может быть полезен, если вы хотите воспользоваться тем же самым отображением для нескольких ресурсов 
    и передавать данные для изменения его поведения в каждом отдельном случае (ниже, мы передаем разные имена шаблонов).

    url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),

[➤ Передача дополнительных опций для просмотра функций]()




**▪ Импортировать в файл контроллера views.py модели** 

    from .models import Book, Author, BookInstance, Genre
  
**▪ Пример функции обработчика index()**

    def index(request):
        Выборка данных из базы 
        Model.objects.all().count()
        Model.objects.filter(status__exact='a')
        
       ...
        Отрисовка HTML-шаблона index.html с данными внутри переменной контекста context
        
        return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
 
☛ [render()](https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#django.shortcuts.render) - функцию, которая генерирует HTML-файлы при помощи шаблонов страниц и соответствующих данных.

#### ✓ Язык шаблонов Django

◾ Расширение базового шаблона

    {% extends "base_generic.html" %}

◾ Подключение статических файлов (css-стили, скрипты)

    {% load static %}
    
    <link href='{% static "css/base.css" %}'rel="stylesheet">

◾ Базовый блок

    {% block sidebar %}
            ...
    {% endblock %}

◾ Условные ветвления 

    {% if УСЛОВИЕ %}
      <!-- здесь наш код "бежит" по списку книг -->
    {% else %}
      <p>В библиотеке книг нет.</p>
    {% endif %}

◾ Отображение переменных контекста

    {{ num_books }}

◾ Генератор ссылок

    <a href="{% url 'books' %}">All books</a>

◾ Цикл For

    {% for book in book_list %}
       <a href="{{ book.get_absolute_url }}">{{ book.title }}</a> ({{book.author}})
    {% endfor %}
 

⚠ Примечание. Переменные шаблона заключаются в двойные фигурные скобки ({{ num_books }}) , 
  а тэги шаблона (функции шаблона), помещаются в одинарные фигурные скобки со знаками процента ({% extends "base_generic.html" %}).

[➤ Справочник по встроенным тегам](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/)

#### ✓ Разработка страниц сайта

◆ **Разработка главной страницы**

▸ Разработать шаблон base.html

▹ Подключить статику

▹ Обозначить блоки приложения

▸ Разработать шаблоны index.html, item_list.html, detail.html

▹ Расширить шаблон base.html

▹ Обозначить блоки страници

▹ Вывести переменные контекста

▹ Сделать логическую проверку

▹ Вывести содержимое базы данных в цикле



 



#### ✓ Создание страницы co списком содержимого
    
⚬ Перенастроить пути с приминением подключонного модуля

    
    
**●  Отображение (на основе базового класса)**

    from django.views.generic import (ListView, DetailView)
    
▪ Выводим общий список компонентов

    class BookListView(ListView):
        ...
        
☛ get_queryset() - метод получения списка всех записей.

    def get_queryset(self):
            return Book.objects.all()
            
☛ get_context_data() - отвечает за переменную контекста.

     def get_context_data(self, **kwargs):   
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context     
    
⚬ В первую очередь - получить существующий контекст из нашего суперкласса.
⚬ Затем добавить в контекст новую информацию.
⚬ Затем вернуть новый (обновленный) контекст.

▪ Выводим детальную информацию комонента
 
    class BookDetailView(DetailView):
        ...
    
        model = Book
        context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
        queryset = Book.objects.filter(status__exact='a')[:5] # Получение 5 книг
        template_name = 'books/index.html'  # Определение имени вашего шаблона и его расположения
        


[➤ Ссылки по теме](https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-display/) 


✔ - основной шаг плана  
◆ - раздел
▸ - пункт действия
▹ - подпункты дейтвия
☛ - определение, важная функйия
➤ - ссылка
✎ - заметка


▸ ▹
● ◆ ◇ ◦ ◌
◻ ◼ ◽ ◾ ■ □  ☐ ☑ ☒
▬ ☛ ✔ ✓ ❖
⇿ ❓