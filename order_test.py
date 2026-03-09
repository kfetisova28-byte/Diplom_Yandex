import data
import sender_stand_request

def test_create_and_get_order():
    # Шаг 1. Создаём заказ
    order = sender_stand_request.create_order(data.order_body)
    
    
    # Шаг 2. Получаем трек‑номер из ответа
    track_number = order.json()["track"]
    print(f"Номер вашего заказа: {track_number}")
    
    
    # Шаг 3. Получаем данные заказа по треку
    response = sender_stand_request.get_data_order_with_track(track_number)
    
    
    # Шаг 4. Проверяем, что код ответа равен 200
    assert response.status_code == 200, f"Запрос не прошёл, ошибка: {response.status_code}"
    
    
    # Шаг 5. Выводим данные заказа
    order_data = response.json()
    print(f"Данные вашего заказа: {order_data}")

    #Фетисова Кристина Андреевна, 41 когорта, дипломная работа