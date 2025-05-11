import pytest
import re
from booking import generate_booking_ref

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