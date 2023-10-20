# Андрей Корниенко, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


def post_new_order(body):  #Создание заказа
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                          json=body)


def get_order(track_number):  #Заказ по номеру трекера
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


def test_order():
    response = post_new_order(data.order_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

    order_response = get_order(track_number)   #Получение трека

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)