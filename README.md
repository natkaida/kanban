# Kanban-доска на Django, DRF & Alpine.js 

## [Туториал для Selectel](https://selectel.ru/blog/tutorials/develop-canban-board-on-django-drf-alpine-js/)

![kanban1](https://user-images.githubusercontent.com/85797091/206715749-f5d4e15f-8d01-4d6c-ae4a-b58e8ab334e3.png)

### Установка локального окружения

```bash
git clone https://github.com/natkaida/kanban.git
cd kanban

pip install -r requirements.dev.txt
python3 manage.py migrate
python3 manage.py createsuperuser
```

После изменений перед комитом выполнить `flake8`, поправить перечисленные им ошибки, для поддержания кода в едином стиле.

### Продакшн

1. Установить зависимости `pip install -r requirements.txt`
1. Создать файл конфигурации `local_settings.py` в папке [kanban](kanban) по примеру из файла [kanban/local_settings.py.example](kanban/local_settings.py.example).
1. Собрать статику командой `python3 manage.py collectstatic`, после чего она будет доступна в папке `./static`.
