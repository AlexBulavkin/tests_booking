from unittest.mock import patch
from booking import send_notification_email

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