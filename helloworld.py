from functions import Functions
class HelloWorld:
    def __init__(self):
        pass
    def displ(self):
        # print("Assalam-O-Alaikum WorlD")
        fun = Functions()
        print(fun.displ("Syed Muhammad Faraz Hashmi"))

# hw = HelloWorld()
# hw.displ()
fun = Functions()
# fun.namazCalculator(1990)
# print(fun.displ(enteryourname="SMFH"))
print("Price per item is: ", str(fun.costCalculator(fun.getInputFromUser(enterStatement="Enter the price of the product: "), fun.getInputFromUser(enterStatement="Enter total quantity of the items: "))))
