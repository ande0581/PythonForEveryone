class Dog:
    __doc__ = "This is my dog definition"

    # This is what gets called when a class is instantiated (Common) known as Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{} constructed!\n".format(self.name))

    def dog_years(self):
        print("{} is {} in dogs years".format(self.name, self.age*7))

    def bark(self):
        print("{} goes Woof Woof!".format(self.name))

    def sleep(self):
        print("{} is taking a nap".format(self.name))

    # Uncommonly used, known as Destructor
    def __del__(self):
        print('This is what happens when a class gets destroyed')


class Child(Dog):
    __doc__ = "This is child class of Dog to demonstrate inheritance"

    def sit(self):
        print("{} sits down.".format(self.name))


# Instantiate the main class
boston = Dog('Jim', 7)
yorkie = Dog('Jan', 2)
frenchie = Dog('Jake', 1)
bcollie = Dog('Jessie', 11)

dogs = [boston, yorkie, frenchie, bcollie]

for dog in dogs:
    dog.dog_years()
    dog.bark()
    dog.sleep()
    print('')

# Instantiate a child class that inherits from the parent class being passed into it
golden = Child('Rusty', 7)
golden.dog_years()
golden.bark()
golden.sleep()
golden.sit()


