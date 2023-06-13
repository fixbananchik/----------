class noda:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BT:
    def __init__(self):
        self.head = None

    def push(self, number):
        new_noda = noda(number)
        if self.head == None:
            self.head = new_noda
        else:
            current = self.head
            while current:
                if new_noda.value <= current.value:
                    if current.left == None:
                        current.left = new_noda
                        break
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = new_noda 
                        break
                    else:
                        current = current.right

    
                        


    


derevo = BT()
derevo.push(5)
derevo.push(4)
derevo.push(6)
1