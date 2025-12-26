# Task 1 and Task 2 : Membuat kelas order yang representatif beserta atributnya
from platform import processor


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


# Task 3
class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        total = 0.0
        for order in self.orders:
            total += order.total_amount
        return total

    def calculate_total_tax(self, tax_rate):
        tax_total = 0.0
        for order in self.orders:
            tax_total += order.calculate_tax(tax_rate)
        return tax_total

    def display_orders(self):
        for i, order in enumerate(self.orders, start=1):
            print(f"\n--- Order #{i} ---")
            print(order.display_order())


def main_menu(tax_rate=0.11):
    print("\n===== MAIN MENU =====\n")
    print(f"1. Ubah Pajak ({tax_rate*100:.0f}%)")
    print("2. Tambahkan Order")
    print("3. Hitung Pendapatan Total dan Pajak")
    print("4. Tampilan Orders")
    print("5. Keluar")
    return int(input("\nPilih opsi (1-5): "))


def input_order():
    order_id = input("Masukkan Order ID: ")
    customer_name = input("Masukkan Customer Name: ")
    order_date = input("Masukkan Tanggal Order (YYYY-MM-DD): ")
    total_amount = float(input("Masukkan Total Transaksi: "))
    return Order(order_id, customer_name, order_date, total_amount)


def main():
    tax_rate = 0.11  # 11% defeault tax rate
    ui = main_menu(tax_rate)
    processor = OrderProcessor()
    while True:
        if ui == 1:
            tax_rate = float(input("Ubah tax rate (0.00-1.00): "))
            print(f"Tax rate berhasil diubah menjadi {tax_rate*100:.0f}%")
            ui = main_menu(tax_rate)
        elif ui == 2:
            order = input_order()
            processor.add_order(order)
            print("Order berhasil ditambahkan.")
            user_order_choice = input(
                "Apakah Anda ingin menambahkan order lain? (y/n): "
            )
            if user_order_choice.lower() == "y":
                ui = 2
            else:
                ui = main_menu(tax_rate)
        elif ui == 3:
            total_revenue = processor.calculate_total_revenue()
            print(f"Total Revenue : {total_revenue:,.2f}")
            total_tax = processor.calculate_total_tax(tax_rate)
            print(f"Total Tax ({tax_rate*100:.0f}%) : {total_tax:,.2f}")
            user_order_choice = input(
                "Apakah Anda ingin melihat detail transaksi? (y/n): "
            )
            if user_order_choice.lower() == "y":
                ui = 4
            else:
                ui = main_menu(tax_rate)
        elif ui == 4:
            print("\n===== DETAIL PESANAN =====")
            processor.display_orders()
            user_order_choice = input(
                "Apakah Anda ingin melihat besaran nilai transaksi? (y/n): "
            )
            if user_order_choice.lower() == "y":
                ui = 3
            else:
                ui = main_menu(tax_rate)
        elif ui == 5:
            break


if __name__ == "__main__":
    main()
