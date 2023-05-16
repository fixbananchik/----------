class noda:
    def __init__(self, value, count):
        self.value = value
        self.link = None
        self.count = count


class str_list:
    def __init__(self):
        self.head = None

    def push(self, storka, count):
        new_noda = noda(storka, count)
        if self.head == None:
            self.head = new_noda
            self.count = count
        else:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = new_noda

    def pop(self):
        if self.head == None:
            pass
        else:
            current = self.head
            prev = None
            while current.link != None:
                prev = current
                current = current.link
            prev.link = None

    def print(self):
        if self.head == None:
            print('список пуст')
        else:
            index = 0
            current = self.head
            while current.link != None:
                print(index, current.value, current.count)
                current = current.link
                index = index + 1
            print(index, current.value, current.count)

    def find(self, element_name):
        if self.head == None:
            return False
        else:
            current = self.head
            while current.link != None:
                if current.value == element_name:
                    return True
                current = current.link
            if current.value == element_name:
                return True
            else:
                return False
                
            




hleb = noda("хлеб", 2)
maslo = noda("масло", 1)
smetana = noda("сметана", 3)
luk = noda("лук", 4)

Magazin = str_list()
Magazin.push("хлеб", 2)
Magazin.push("масло", 1)
Magazin.push("сметана", 3)
Magazin.push("лук", 4)

Magazin.print()