# # Wrong Code
# class myperson:
#     def __init__(self, name, age, gender):
#         self.name=name
#         self.age=age

#     def GetName(self):
#         self.AskedForName = True
#         return self.name


# print(myperson("Abhi",20,"m").GetName())
# To Run this code, type pylint pylint_basics in terminal
"""My perfect code example

This should eventually get 10/10 points
"""

class MyPerson:
    """
    Person Class
    """
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.asked_for_name = False
        self.AskedForAge = False # pylint: disable=invalid-name

    def get_name(self):
        """
        Returns the name of the person
        :return: the name
        """
        self.asked_for_name = True
        return self.name

    def get_age(self):
        """
        Returns the age of the person
        :return: the age
        """
        self.AskedForAge = True
        return self.age

print(MyPerson("Abhi",20,"m").get_name())

# Wrong Code But disable
#pylint: disable=missing-module-docstring
class myperson: # pylint: disable=invalid-name disable=missing-class-docstring disable=too-few-public-methods
    def __init__(self, name, age, gender): # pylint: disable=unused-argument
        self.name=name
        self.age=age

    def GetName(self): # pylint: disable=missing-function-docstring
        self.AskedForName = True # pylint: disable=attribute-defined-outside-init
        return self.name


print(myperson("Abhi",20,"m").GetName()) # pylint: disable=missing-final-newline