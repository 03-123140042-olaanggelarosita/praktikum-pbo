from abc import ABC, abstractmethod

# Kelas abstrak Plant
class Plant(ABC):
    def __init__(self, name, water_needs, fertilizer_needs):
        self.name = name  # Nama tanaman
        self.water_needs = water_needs  # Kebutuhan air standar (liter)
        self.fertilizer_needs = fertilizer_needs  # Kebutuhan pupuk standar (kg)
    
    @abstractmethod
    def grow(self):
        pass
    
    def calculate_needs(self, rainfall, soil_moisture):
        # Menyesuaikan kebutuhan air dan pupuk berdasarkan curah hujan dan kelembapan tanah
        if rainfall > 5:  # Jika curah hujan cukup tinggi (lebih dari 5 mm)
            self.water_needs -= 5  # Kurangi kebutuhan air
            if self.water_needs < 0:
                self.water_needs = 0  # Pastikan kebutuhan air tidak negatif
        
        if soil_moisture > 50:  # Jika kelembapan tanah cukup tinggi (lebih dari 50%)
            self.fertilizer_needs -= 1  # Kurangi kebutuhan pupuk
            if self.fertilizer_needs < 0:
                self.fertilizer_needs = 0  # Pastikan kebutuhan pupuk tidak negatif
    
    def show_needs(self):
        # Menampilkan kebutuhan air dan pupuk yang sudah disesuaikan
        print(f"Adjusted Water Needs: {self.water_needs} liters")
        print(f"Adjusted Fertilizer Needs: {self.fertilizer_needs} kg")

# Kelas turunan RicePlant
class RicePlant(Plant):
    def __init__(self):
        super().__init__("Rice", 20, 5)  # Kebutuhan air dan pupuk untuk tanaman padi
    
    def grow(self):
        print(f"{self.name} is growing in the paddy field")

# Kelas turunan CornPlant
class CornPlant(Plant):
    def __init__(self):
        super().__init__("Corn", 25, 7)  # Kebutuhan air dan pupuk untuk tanaman jagung
    
    def grow(self):
        print(f"{self.name} is growing in the farm")

# Simulasi kondisi cuaca
def simulate_weather():
    # Simulasi kondisi cuaca untuk tanaman
    rainfall = float(input("Enter the rainfall (in mm): "))  # Curah hujan dalam mm
    soil_moisture = float(input("Enter the soil moisture percentage: "))  # Kelembapan tanah dalam persen
    return rainfall, soil_moisture

# Main Program
def main():
    # Membuat objek tanaman
    rice = RicePlant()
    corn = CornPlant()

    # Menyimulasikan kondisi cuaca untuk tanaman padi
    print("\nSimulating Rice Plant Weather:")
    rainfall, soil_moisture = simulate_weather()
    rice.grow()
    print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
    rice.calculate_needs(rainfall, soil_moisture)
    rice.show_needs()

    # Menyimulasikan kondisi cuaca untuk tanaman jagung
    print("\nSimulating Corn Plant Weather:")
    rainfall, soil_moisture = simulate_weather()
    corn.grow()
    print(f"Weather Report: Rainfall = {rainfall} mm, Soil Moisture = {soil_moisture}%")
    corn.calculate_needs(rainfall, soil_moisture)
    corn.show_needs()

# Menjalankan program
if __name__ == "__main__":
    main()
