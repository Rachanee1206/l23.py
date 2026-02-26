class class1:
   _x=100 #private vars
   def __method(self):
    print("Inside class")
   def method2(self):
    print("Private variable:", class1.__x)

obj=class1()
obj.method2()
obj.__method()

#private vars

#error