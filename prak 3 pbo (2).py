from abc import ABC, abstractmethod

# Kelas induk Employee
class Employee(ABC):
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name  # Nama karyawan
        self.role = role  # Peran karyawan (Software Engineer, Data Scientist, Product Manager)
        self.hours_worked = hours_worked  # Jam kerja
        self.task_completed = task_completed  # Jumlah tugas yang diselesaikan
    
    @abstractmethod
    def work(self):
        pass
    
    def evaluate_performance(self):
        # Menilai performa berdasarkan jam kerja dan jumlah tugas yang diselesaikan
        performance_ratio = self.task_completed / self.hours_worked if self.hours_worked != 0 else 0
        
        # Menilai performa berdasarkan rasio
        if performance_ratio >= 1.5:  # High Performance: Rasio tugas per jam sangat tinggi
            return "High Performance"
        elif performance_ratio >= 1.0:  # Medium Performance: Rasio tugas per jam cukup baik
            return "Medium Performance"
        else:
            return "Low Performance"
    
    def show_performance(self):
        performance = self.evaluate_performance()
        print(f"{self.name} ({self.role}) is {self.get_task_description()}.")
        print(f"Performance Rating: {performance}\n")
    
    @abstractmethod
    def get_task_description(self):
        pass


# Kelas turunan SoftwareEngineer
class SoftwareEngineer(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Software Engineer", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} (Software Engineer) is coding.")
    
    def get_task_description(self):
        return "coding"


# Kelas turunan DataScientist
class DataScientist(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Data Scientist", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} (Data Scientist) is analyzing data.")
    
    def get_task_description(self):
        return "analyzing data"


# Kelas turunan ProductManager
class ProductManager(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Product Manager", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} (Product Manager) is managing the product roadmap.")
    
    def get_task_description(self):
        return "managing the product roadmap"


# Main Program untuk menilai performa karyawan
def main():
    # Membuat objek karyawan dengan berbagai peran
    se = SoftwareEngineer("Alice", 40, 60)  # Alice sebagai Software Engineer
    ds = DataScientist("Bob", 45, 40)  # Bob sebagai Data Scientist
    pm = ProductManager("Charlie", 50, 45)  # Charlie sebagai Product Manager
    se2 = SoftwareEngineer("David", 40, 20)  # David sebagai Software Engineer

    # Menampilkan pekerjaan masing-masing karyawan dan menilai performanya
    se.show_performance()
    ds.show_performance()
    pm.show_performance()
    se2.show_performance()


# Menjalankan program
if __name__ == "__main__":
    main()
