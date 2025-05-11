from unittest.mock import patch
from booking import apply_promo_code

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