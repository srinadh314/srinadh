class PaymentSystem:
    def process_payment(self, amount):
        # Simulate processing payment
        print(f"Processing payment of ${amount}...")
        print("Payment successful!")
        return True

# Example usage:
payment_system = PaymentSystem()

# Simulate payment for an order
order_total = 30
payment_successful = payment_system.process_payment(order_total)

if payment_successful:
    print("Order successfully paid.")
else:
    print("Payment failed. Please try again.")
