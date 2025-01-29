class Currency:
    def __init__(self,n,p):
        self.name=n
        self.price=p
        
    def printInfo(self):
        print("Name :",self.name)
        print("Price :",self.price)
        
b1=Currency("BitCoin",880000.00)
b2=Currency("Ethereum",279470.75)


b1.printInfo()
print()
b2.printInfo()