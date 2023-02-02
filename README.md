# django_to_do_list

### Шаги для запуска: ### 

1. Запустите Docker

1. Убедитесь, что порты 5432, 8000 не заняты, если заняты - освободите

2. В командной строке перейдите в директорию с проектом

3. Установите необходимые пакеты выполнив команду-  
`pip install -r requirements.txt`

4. Создайте Docker контейнер с postgres выполнив команду-  
`python create_DB.py`

5. Выполние миграцию данных в базу данных выполнив команды-   
`python my_task_list/manage.py makemigrations`  
`python my_task_list/manage.py migrate`

6. Создайте пользователя admin  
`python my_task_list/manage.py createsuperuser`

7. Зпапустите приложение  
`python my_task_list/manage.py runserver`

### Главная страница приложения- ###
http://127.0.0.1:8000/

### Admin Site- ###
http://127.0.0.1:8000/admin/
