# Exercise 1: Laptop and battery

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

    class Battery:
        def __init__(self, amount):
            self.level = 100
            self.amount = amount
                    
        def charge(self):
            if  0 <= self.level <100:
                print('Charging Laptop!')
            else: 
                print('Laptop is fully charged')
        
        def drain(self, amount):
            self.level -= amount

        def battery(self):
            return self.level
        
    def use(self):
        self.battery.drain()

laptop = Laptop("Dell", "XPS")
print(laptop.brand)
# laptop.use()
# laptop.battery.charge()
