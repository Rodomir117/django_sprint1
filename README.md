# Blogicum

## Проект django_sprint1

* добавлена ветка **category** в которой посты отображаются по категориям
* словарь POSTS вынесен в **blog/posts_list.py**
* в папке pages отсутствует файл **views.py**, потому что  в файле pages/urls.py используется встроенный класс **TemplateView**    
* в папках pages и blog отсутсвуют файлы: **admin.py, models.py, tests.py**, потому что в проекте они не используются
* в файле .gitignore в 150 строке добавленно исключение для папки **html/**, чтобы удалить папку html из репозитория GitHub используется команда:

      git rm --cached -r html

## Инструкция для пользователей Windows

 1.Клонировать репозиторий и перейти в папку **django_sprint1**:

        git clone git@github.com:Rodomir117/django_sprint1.git
        cd django_sprint1

2.Cоздать и активировать виртуальное окружение:

        py -m venv .venv
        source .venv/Scripts/activate

3.Установить зависимости из файла requirements.txt:

        pip install -r requirements.txt

4.Перейти в папку проекта **blogicum** и запустить его:

        cd blogicum
        ./manage.py migrate
        ./manage.py runserver

5.Перейти на локальный сервер:

        http://127.0.0.1:8000/