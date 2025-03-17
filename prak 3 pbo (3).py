# Kelas BankAccount merepresentasikan akun bank dengan berbagai fitur
class BankAccount:
    # Kurs tetap untuk konversi mata uang
    exchange_rates = {
        'USD': {'EUR': 0.85, 'IDR': 14000},  # Kurs dari USD ke EUR dan IDR
        'EUR': {'USD': 1.18, 'IDR': 16500},  # Kurs dari EUR ke USD dan IDR
        'IDR': {'USD': 0.000071, 'EUR': 0.000061}  # Kurs dari IDR ke USD dan EUR
    }

    def __init__(self, account_holder, balance, currency):
        # Inisialisasi atribut akun bank
        self.account_holder = account_holder  # Nama pemilik akun
        self.balance = balance  # Saldo awal dalam mata uang tertentu
        self.currency = currency  # Mata uang akun

    def __add__(self, amount):
        # Operator overloading untuk menambahkan saldo
        if isinstance(amount, (int, float)):
            self.balance += amount
        return self

    def __sub__(self, amount):
        # Operator overloading untuk mengurangi saldo
        if isinstance(amount, (int, float)):
            self.balance -= amount
        return self

    def convert_currency(self, amount, target_currency):
        # Metode untuk mengonversi mata uang
        if self.currency == target_currency:
            return amount
        if target_currency in self.exchange_rates[self.currency]:
            return amount * self.exchange_rates[self.currency][target_currency]
        raise ValueError("Currency conversion not supported.")

    def apply_interest(self):
        # Menerapkan bunga berdasarkan saldo akun
        if self.balance < 5000:
            interest_rate = 0.01  # 1% untuk saldo di bawah $5000
        else:
            interest_rate = 0.02  # 2% untuk saldo di atas $5000
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Interest applied: {interest:.2f} {self.currency}")

    def withdraw(self, amount, target_currency):
        # Menarik dana dalam mata uang tertentu setelah konversi
        converted_amount = self.convert_currency(amount, target_currency)
        if converted_amount > self.balance:
            print("Insufficient funds for this transaction.")
            return
        self.balance -= converted_amount
        print(f"Withdrew {amount} {target_currency}. New balance: {self.balance:.2f} {self.currency}")

    def check_balance(self):
        # Mengecek saldo dan memberi peringatan jika rendah
        if self.balance < 100:
            print("Low Balance Warning!")
        print(f"Current balance: {self.balance:.2f} {self.currency}")

# Contoh penggunaan
if __name__ == "__main__":
    # Akun John dengan saldo dalam USD
    john_account = BankAccount("John", 5000, "USD")
    john_account.apply_interest()  # Menerapkan bunga
    john_account.check_balance()  # Mengecek saldo

    print()  # Pemisah output

    # Akun Emily dengan saldo dalam EUR
    emily_account = BankAccount("Emily", 1000, "EUR")
    emily_account.withdraw(1200, "USD")  # Mencoba menarik $1200 setelah konversi
    emily_account.check_balance()  # Mengecek saldo setelah transaksi


# 122140171