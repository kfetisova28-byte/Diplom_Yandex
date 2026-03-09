# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests
import data


def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,      # Создание заказа
                         json=body)


def get_data_order_with_track(track_number):
    url_get_order = f"{configuration.URL_SERVICE}{configuration.GET_ORDER}{track_number}"    # Получение данных о заказе по трек‑номеру
    return requests.get(url_get_order)
