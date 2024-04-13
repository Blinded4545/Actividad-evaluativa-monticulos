

class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.dir = None
        self.severity = None
        self.priority = None

    def evalIntegers(self, i):
        try:
            int(i)
            return True
        except:
            return False

    def assignValues(self):
        self.name = input("Introduce el nombre completo de la persona: ")

        # Set age value
        ageInput = False

        while not ageInput:
            ageVal = input("Introduce la edad de la persona: ")
            ageInput = self.evalIntegers(ageVal)
            if ageInput:
                ageVal = int(ageVal)
                if ageVal < 1 or ageVal > 100:
                    print("Edad invalida, vuelve a introducirla.")
                    ageInput = False
                    ageVal = None
                else:
                    print(ageVal)
                    self.age = ageVal
            else:
                print("Edad invalida, introducela nuevamente: ")

        # Set dir value
        self.dir = input("Introduce la direccion de la persona: ")

        # Set severity value
        severityInput = False
        while not severityInput:
            severityVal = input("Introduce la severidad de la persona del 1 al 5: ")
            severityInput = self.evalIntegers(severityVal)
            if severityInput:
                severityVal = int(severityVal)
                if severityVal < 1 or severityVal > 5:
                    severityInput = False
                    print("Valor de severidad incorrecto, intenta de nuevo.")
                else:
                    self.severity = severityVal
            else:
                print("Valor de severidad incorrecto, intenta de nuevo.")

        # Set priority value
        if self.age < 12:
            self.priority = 1

        elif self.age > 65:
            self.priority = 2

        else:
            self.priority = 3

    def printValues(self):
        print("Nombre: " + self.name +
              "\nEdad: " + str(self.age) +
              "\nDirección: " + self.dir +
              "\nSeveridad: " + str(self.severity) +
              "\nPrioridad: " + str(self.priority) +
              "\nUnidad de transporte: " + self.unit() +
              "\n")

    def unit(self):
        if self.severity < 3:
            return "Patrulla y unidades de refuerzo"
        else:
            return "Unidad motorizada"
