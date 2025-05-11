import random
import string

def calc_price(base_price: float, discount: float, count: int) -> float:
    if count <= 0 or base_price < 0 or discount < 0 or discount > 1:
        raise ValueError("Invalid input")
    return base_price * count * (1 - discount)

def check_availability(event_id: int, seats_requested: int) -> bool:
    available_seats = get_available_seats(event_id)
    return seats_requested <= available_seats

def get_available_seats(event_id: int) -> int:
    return 100

def apply_promo_code(order_id: int, promo_code: str) -> bool:
    promo = get_promo(promo_code)
    if not promo or promo["expired"] or promo["used"] >= promo["limit"]:
        return False
    promo["used"] += 1
    return True

def get_promo(code: str):
    return {"expired": False, "limit": 5, "used": 2}

def generate_booking_ref(user_id: int, event_id: int) -> str:
    if user_id < 0 or event_id < 0:
        raise ValueError("User ID and Event ID must be non-negative")
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"BOOK-{user_id}-{event_id}-{suffix}"

def send_notification_email(email: str, booking_details: dict) -> bool:
    try:
        send_email(email, booking_details)
        return True
    except Exception:
        return False

def send_email(email: str, details: dict):
    pass