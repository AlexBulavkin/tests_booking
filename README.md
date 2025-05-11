# Booking Service Tests

## Как запускать тесты

1. Установите зависимости:
```
pip install -r requirements.txt
```

2. Запустите тесты:
```
pytest
```

## Что тестируем

- `calc_price`: расчет с учетом скидки
- `check_availability`: проверка свободных мест (с использованием mock)
- `apply_promo_code`: применение промокода (mock базы промокодов)
- `generate_booking_ref`: генерация уникального кода
- `send_notification_email`: отправка почты (mock SMTP)