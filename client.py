from typing import Dict, Any

class GiftWrapCalculatorClient:
    def calculate_gift_wrap(self, style: str, message: str) -> Dict[str, Any]:
        styles = {
            "premium": 5.99,
            "standard": 2.99,
            "none": 0.00
        }
        wrap_fee = styles.get(style.lower(), 0.00)
        char_count = len(message.strip())
        message_fee = 0.0
        if char_count > 100:
            # Surcharge for long customized note cards
            message_fee = 1.50
        return {
            "wrap_fee": wrap_fee,
            "card_message_fee": message_fee,
            "total_gift_service_fee": round(wrap_fee + message_fee, 2)
        }
