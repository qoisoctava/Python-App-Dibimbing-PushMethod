# Task 1 and Task 2 : Membuat kelas order yang representatif beserta atributnya
class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = str(order_id)
        self.customer_name = str(customer_name)
        self.order_date = str(order_date)
        self.total_amount = float(total_amount)

    # Task 2 : Menghitung dan mengembalikan jumlah pajak berdasarkan jumlah total dan tarif pajak yang diberikan
    def calculate_tax(self, tax_rate):
        return (
            self.total_amount * tax_rate if (0 <= tax_rate <= 1) else "invalid tax rate"
        )

    # Task 2 : Mencetak detail pesanan dalam format yang mudah digunakan
    def display_order(self):
        output = {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "order_date": self.order_date,
            "total_amount": self.total_amount,
        }
        return output


def main():
    o1 = Order("ORD-001", "Bambang", "2025-12-18", 250000)
    # print(o1.order_id, o1.customer_name, o1.total_amount)
    print(o1.display_order())


if __name__ == "__main__":
    main()
