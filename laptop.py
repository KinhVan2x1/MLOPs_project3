# Exercise 1: Laptop and battery

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = self.Battery()
        
    class Battery:
        def __init__(self, amount=5):
            self.level = 100
            self.amount = amount
        
        def status(self):
            return f"{self.level}"
                                
        def charge(self):
            if  0 <= self.level <100:
                print('Charging Laptop!')
                self.level = min(100, self.level +5)
            else: 
                print('Laptop is fully charged')
        
        def drain(self):
            self.level = max(0, self.level - self.amount)

               
    def use(self):
        if self.battery.level <= 0:
            print('Please charge first!')
            return 
        self.battery.drain()
        print(f'Current battery level: {self.battery.level}%')



laptop = Laptop("Dell", "XPS")
laptop.use()
laptop.battery.charge()


