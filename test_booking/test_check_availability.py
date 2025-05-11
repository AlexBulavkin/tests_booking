from unittest.mock import patch
from booking import check_availability

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