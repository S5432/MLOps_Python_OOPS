class Employee():
    # special method/magic method/ dunder method - constructor.
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation= "SDE"
        print("Attributes/data have been initiated")
    
    def travel(self, destination):
        print("This travel method was called manually.")
        print(f"Employee is now travelling to {destination}")

# create an obj/instance of the class
sam = Employee()

# printing the attributes
#print(sam.id)

# calling a method
sam.travel("Kerala")