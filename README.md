# Как использовать

## Зависимости - mako, weasyprint, flask(необязательно)

`pip install mako weasyprint # pip install flask`

### В файле **data.py** находится пример входных дынных. Дынные прокидываются в функцию **index** в файле **app.py**. В результате получаем pdf файл с именем по типу _19-03-2023-17_43.pdf_(дата и время создания документа). **!Важно, чтобы все поля, как в примере data.py были заполнены.**

### Для дебага и дополнений в **app.py** имееются комментарии для **flask** сервера. При его запуске создаться локальный сервер **http://localhost:5000** с html и css кодом, где можно в live режиме менять стили и html
