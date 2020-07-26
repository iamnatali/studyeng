# studyeng

#### Doubletapp
#### Тестовое задание: Backend

rest-api сайта для обучения английскому

Теперь приложение доступно на https://marideldaicher.pythonanywhere.com/

Pythonanywhere разрешает доступ только через прокси-сервер proxy.server:3128

пример обращения к /categories/ можно найти в файле test.py

Для запуска проекта из докера по очереди выполнить:

* docker-compose build
* docker-compose up -d db
* docker-compose up -d web
* docker-compose up
