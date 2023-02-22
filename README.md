# HTML to pdf

## Зависимости - mako, weasyprint, flask(необязательно)

`pip install mako weasyprint # pip install flask`

В файле **data.py** находится пример входных дынных. Дынные прокидываются в функцию **index** в файле **app.py**. В результате получаем pdf файл с именем по типу [21-02-2023-19_42.pdf](https://github.com/Tinkerbells/html-to-pdf/blob/main/21-02-2023-19_42.pdf) (дата и время создания документа). **!Важно, чтобы все поля, как в примере data.py были заполнены.**

Для дебага и дополнений в **app.py** имееются комментарии для **flask** сервера. При его запуске создаться локальный сервер **http://localhost:5000** с html и css кодом, где можно в live режиме менять стили и html

### Определяем дату

`data = {...}`

### Вызываем функцию index

`from app import index
index(data)`
