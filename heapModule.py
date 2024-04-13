
from personModule import Person
from os import system


class heap:

    def __init__(self):
        # Binary Search Tree
        self.BST = [0]
        self.currSize = 0

    def filterAdd(self, index):
        while index // 2 > 0:
            if self.BST[index // 2].severity == self.BST[index].severity:
                if self.BST[index // 2].priority > self.BST[index].priority:
                    tmp = self.BST[index // 2]
                    self.BST[index // 2] = self.BST[index]
                    self.BST[index] == tmp

            elif self.BST[index // 2].severity > self.BST[index].severity:
                tmp = self.BST[index // 2]
                self.BST[index // 2] = self.BST[index]
                self.BST[index] = tmp

            index = index // 2

    def addPerson(self, person):
        self.BST.append(person)
        self.currSize += 1
        self.filterAdd(self.currSize)

    def filterMin(self, index):
        while (index * 2) <= self.currSize:
            iMin = self.minIndex(index)
            if self.BST[iMin].severity == self.BST[index].severity:
                if self.BST[iMin].priority < self.BST[index].priority:
                    tmp = self.BST[index]
                    self.BST[index] = self.BST[iMin]
                    self.BST[iMin] = self.BST[index]

            elif self.BST[iMin].severity < self.BST[index].severity:
                tmp = self.BST[index]
                self.BST[index] = self.BST[iMin]
                self.BST[iMin] = tmp

            index = iMin

    def minIndex(self, index):
        if index * 2 + 1 > self.currSize:
            return index * 2
        else:
            if self.BST[index * 2].severity == self.BST[index * 2 + 1].severity:
                if self.BST[index * 2].priority < self.BST[index * 2 + 1].priority:
                    return index * 2
                else:
                    return index * 2 + 1

            if self.BST[index * 2].severity < self.BST[index * 2 + 1].severity:
                return index * 2

            return index * 2 + 1

    def attendPerson(self):
        if self.currSize < 1:
            print("\nNo hay personas por atender.\n")
            return

        select = self.BST[1]
        self.BST[1] = self.BST[self.currSize]
        self.currSize -= 1
        self.BST.pop()
        self.filterMin(1)
        select.printValues()

    def buildBST(self, list):
        i = len(list) // 2
        self.currSize = len(list)
        self.BST = [0] + list[:]
        while i > 0:
            self.filterMin(i)
            i = i - 1

    def showBST(self):
        if self.currSize < 1:
            print("\nNo hay personas por atender.\n")
            return

        for i in self.BST:
            if i != 0:
                i.printValues()


def testFunction():
    bst1 = heap()
    pList = []
    for i in range(3):
        z = Person()
        z.assignValues()
        pList.append(z)

    # for i in pList:
    #     print(i.printValues())

    bst1.buildBST(pList)
    # bst1.showBST()
    bst1.attendPerson()
    bst1.attendPerson()
    bst1.attendPerson()


def functionLoop():
    system("clear")
    bst1 = heap()
    i = 0

    print("Bienvenido a la linea de atencion.")
    while i != 4:
        print("\n1. Ingresar nuevo solicitante")
        print("2. Atender siguiente solicitante")
        print("3. Mostrar lista de solicitantes")
        print("4. Salir")

        try:
            i = int(input("\nIntroduce tu opcion: "))

        except:
            print("La opcion ingresada no existe, intenta nuevamente.\n")

        match i:
            case 1:
                p = Person()
                p.assignValues()
                bst1.addPerson(p)
                system("clear")
                print("Solicitante ingresado exitosamente")

            case 2:
                system("clear")
                print("\nActualmente atendiendo al siguiente solicitante: \n")
                bst1.attendPerson()

            case 3:
                system("clear")
                print("\nMostrando todos los solicitantes: \n")
                bst1.showBST()

            case 4:
                print("Hasta pronto! Feliz dia")

            case _:
                print("La opcion ingresada no existe, intenta nuevamente.\n")


functionLoop()
