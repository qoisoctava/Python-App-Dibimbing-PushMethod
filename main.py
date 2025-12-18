class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = float(total_amount)


def main():
    o1 = Order("ORD-001", "Budi", "2025-12-18", 250000)
    print(o1.order_id, o1.customer_name, o1.total_amount)


if __name__ == "__main__":
    main()
