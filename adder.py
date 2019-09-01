class Valuable():
    def __init__(self, v=0):
        self.val = v
    
    def getValue(self):
        return self.val
    
    def setValue(self):
        self.val = int(input('Enter an integer: '))

def adder(x, y):
    return (x + y)

if __name__ == "__main__":
    val1 = Valuable()
    val2 = Valuable()

    val1.setValue()
    val2.setValue()

    print('Sum of numbers entered: ', adder(val1.getValue(), val2.getValue()))
