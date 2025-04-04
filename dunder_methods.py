class DunderTestClass:

    def __init__(self, a):
        self.a = a

    @staticmethod
    def eg_static_method(self):
        pass

    def __str__(self):
        return f"value = {self.a}"
    
    def __add__(self, dunder_obj):
        return self.a + dunder_obj.a
    
    def __sub__(self, dunder_obj):
        """
        Dunder method for subtraction. Subtracts the value of the other 
        object from the value of this object and returns the result.

        Parameters:
            dunder_obj: The DunderTestClass object to subtract from this object.

        Returns:
            The result of subtracting the other object from this object.
        """
        return self.a - dunder_obj.a

if __name__ == "__main__":

    obj1 = DunderTestClass(10)
    obj2 = DunderTestClass(20)

    print(obj1)
    print(obj1 + obj2)
    print(obj1 - obj2)

    DunderTestClass.eg_static_method()