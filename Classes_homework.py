class Vehicle:
    def __init__(self,Make,Model,Year,Weight,NeedsMaintenance=False,TripsinceMaintenance=0):
   
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsinceMaintenance = TripsinceMaintenance
    #getters
        def getmake(self):
            return self.Make
        def getmodel(self):
            return self.Model
        def Year(self):
            return self.Year
        def Weight(self):
            return self.Weight
        def repair(self):
            self.NeedsMaintenance = False
            self.TripsinceMaintenance = 0
    #setters
        def setmake(self,Make):
            self.Make = Make
        def setmodel(self,Model):
            self.Model = Model
        def setyear(self,Year):
            self.Year = Year
        def Weight(self,Weight):
            self.Weight = Weight

class car(Vehicle):
    def __init__(self,Make,Model,Year,Weight,isdriving=False):
        Vehicle.__init__(self,Make,Model,Year,Weight)
        self.isdriving=isdriving

        def drive(self):
            self.isdriving = True
        def stop(self):
            if self.isdriving:
                self.TripsinceMaintenance +=1
                if  self.TripsinceMaintenance > 100:
                    self.NeedsMaintenance= True
            self.isdriving=False

def randomdrivecar(car):
    drivetimes = random.randint(1,101)
    for i in range(drivetimes):
        car.drive()
        car.stop()

carone  = car("Toyota", "GLI", "2019","2 ton")
cartwo = car("suzuki","CIAZ","2020", "1.5 ton")
carthree = car("Honda", "Civic X","2017", "2.2 ton")

def carprint(car):
    print("Make : ",car.Make)
    print("Model : ",car.Model)
    print("Year : ",car.Year)
    print("Weight : ",car.Weight)
    print("NeedsMaintenance : ",car.NeedsMaintenance)
    print("TripsinceMainteannce : ",car.TripsinceMaintenance)


carprint(cartwo)
carprint(carone)
carprint(carthree)