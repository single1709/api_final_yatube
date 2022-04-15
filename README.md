# Проект «API для Yatube»
## Кратко о проекте
Данный проект - реализация API для другого учебного проекта Yatube.
API необходим для унифицированного доступа к функциям проекта Yatube.
С помощью API можно работать с проектом Yatube при помощи запросов, а не использовать для этого ручные операции.
Наличие API повышает безопасность, универсальность, мобильность и доступность проекта Yatube.

## Как запустить проект
### Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/single1709/api_final_yatube.git```

```cd api_final_yatube```
### Cоздать и активировать виртуальное окружение:

```python3 -m venv env```
```source env/bin/activate```
### Установить зависимости из файла requirements.txt:

```python3 -m pip install --upgrade pip```
```pip install -r requirements.txt```
### Выполнить миграции:

```python3 manage.py migrate```
### Запустить проект:

```python3 manage.py runserver```

## Работа с API
Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube. В документации описано, как работать с API.
Документация представлена в формате Redoc и содержит наглядные примеры запросов.
### Примеры
---
***получение публикации по id***

`GET /api/v1/posts/{id}/`

Response

>Статус 200 - удачное выполнение запроса
```json
{
 "id": 0,   
 "author": "string",  
 "text": "string",  
 "pub_date": "2019-08-24T14:15:22Z",  
 "image": "string", 
 "group": 0 
}
```

>Статус 404 - попытка запроса несуществующей публикации
```json
{
  "detail": "Страница не найдена."
}
```

---
***создание публикации***

`POST /api/v1/posts/`

Request

```json
{
 "text": "string",
 "image": "string",
 "group": 0
}
```
Response

>Статус 200 - удачное выполнение запроса

```json
{
 "id": 0,
 "author": "string",
 "text": "string",
 "pub_date": "2019-08-24T14:15:22Z",
 "image": "string",
 "group": 0
}
```

>Статус 400 - отсутствует обязательное поле в теле запроса

```json
{
 "text": [
    "Обязательное поле."
 ]
}
```

>Статус 401 - запрос от имени анонимного пользователя

```json
{
 "detail": "Учетные данные не были предоставлены."
}
```
---
***удаление публикации***

`DELETE /api/v1/posts/{id}/`

Response

>Статус 204 - удачное выполнение запроса

>Статус 401 - запрос от имени анонимного пользователя
```json
{
 "detail": "Учетные данные не были предоставлены."
}
```
>Статус 403 - попытка изменения чужого контента
```json
{
 "detail": "У вас недостаточно прав для выполнения данного действия."
}
```
>Статус 404 - попытка удаления несуществующей публикации
```json
{
 "detail": "Страница не найдена."
}
```
## Автор
Сергей,

Студент факультета Backend-разработки в Яндекс.Практикум.

## Используемые технологии

* REST
* ORM
