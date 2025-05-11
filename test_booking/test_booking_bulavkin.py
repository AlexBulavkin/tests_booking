import pytest
import re
from unittest.mock import patch
from booking import calc_price, apply_promo_code, check_availability, generate_booking_ref, send_notification_email

@pytest.mark.parametrize("base,discount,count,expected", [
    (100.0, 0.1, 2, 180.0),
    (50.0, 0.2, 4, 160.0),
])
def test_calc_price_positive(base, discount, count, expected):
    assert calc_price(base, discount, count) == expected

@pytest.mark.parametrize("base,discount,count", [
    (-10.0, 0.1, 1),
    (100.0, -0.2, 2),
    (100.0, 1.5, 2),
    (100.0, 0.1, 0),
])
def test_calc_price_negative(base, discount, count):
    with pytest.raises(ValueError):
        calc_price(base, discount, count)

def test_check_availability_positive():
    with patch('booking.get_available_seats', return_value=10):
        assert check_availability(1, 5)

def test_check_availability_exact():
    with patch('booking.get_available_seats', return_value=5):
        assert check_availability(1, 5)

def test_check_availability_negative():
    with patch('booking.get_available_seats', return_value=3):
        assert not check_availability(1, 5)

def test_check_availability_zero_seats():
    with patch('booking.get_available_seats', return_value=0):
        assert not check_availability(1, 1)

def test_apply_promo_code_valid():
    promo = {"expired": False, "limit": 5, "used": 2}
    with patch('booking.get_promo', return_value=promo):
        assert apply_promo_code(1, "SAVE10")

def test_apply_promo_code_limit_edge():
    promo = {"expired": False, "limit": 3, "used": 2}
    with patch('booking.get_promo', return_value=promo):
        assert apply_promo_code(1, "EDGE")

def test_apply_promo_code_expired():
    promo = {"expired": True, "limit": 5, "used": 1}
    with patch('booking.get_promo', return_value=promo):
        assert not apply_promo_code(1, "EXPIRED")

def test_apply_promo_code_over_limit():
    promo = {"expired": False, "limit": 5, "used": 5}
    with patch('booking.get_promo', return_value=promo):
        assert not apply_promo_code(1, "LIMITED")

def test_generate_booking_ref_format():
    ref = generate_booking_ref(10, 20)
    assert re.match(r"BOOK-10-20-[A-Z0-9]{6}", ref)

def test_generate_booking_ref_uniqueness():
    refs = {generate_booking_ref(1, 2) for _ in range(10)}
    assert len(refs) == 10

def test_generate_booking_ref_negative_user_raises():
    with pytest.raises(ValueError, match="User ID and Event ID must be non-negative"):
        generate_booking_ref(-1, 2)

def test_generate_booking_ref_negative_event_raises():
    with pytest.raises(ValueError, match="User ID and Event ID must be non-negative"):
        generate_booking_ref(1, -2)

def test_send_notification_email_success():
    with patch('booking.send_email', return_value=None):
        assert send_notification_email("user@example.com", {"booking_id": 123})

def test_send_notification_email_failure():
    with patch('booking.send_email', side_effect=Exception("SMTP error")):
        assert not send_notification_email("user@example.com", {"booking_id": 123})

def test_send_notification_email_invalid_email():
    with patch('booking.send_email', return_value=None):
        assert send_notification_email("", {"booking_id": 456})

def test_send_notification_email_missing_booking_details():
    with patch('booking.send_email', return_value=None):
        assert send_notification_email("user@example.com", {})