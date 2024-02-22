class Person:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
    def Myfun(self):
        print("My Name is "+ self.Name,self.Age)
p1=Person("sireesha",20)
print(p1.Myfun())

#inheritance
class Parent:
    def __init__(self,surname):
        self.surname=surname
class son(Parent):
    pass
s1=son(kotha)
print(s1)
# nums=[2,7,11,15]

