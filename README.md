# studyeng

#### Doubletapp
#### Тестовое задание: Backend

Для запуска проекта по очереди выполнить:

* docker-compose build
* docker-compose up -d db
* docker-compose up -d web
* docker-compose up

Приложение запустится на http://localhost:8000/

Для входа в admin потребуется создание суперпользователя

NB! Возможно потребуется создание бд со следующими характеристиками и проведение миграций:

* 'ENGINE': 'django.db.backends.postgresql',
* 'NAME': 'test',
* 'USER': 'postgres',
* 'PASSWORD': '36854',
* 'HOST': 'db',
* 'PORT': 5432
