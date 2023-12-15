class Triangle:
    def __init__(self):
        self.a = float
        self.b = float
        self.c = float

    def get_values(self, a, b, c):
        try:
            if a > 0 and b > 0 and c > 0:
                self.a = a
                self.b = b
                self.c = c
            else:
                raise ValueError("Los valores deben ser floats mayores a 0")
        except Exception as E:
            self.a = None
            self.b = None
            self.c = None
            print(E)
            return E


        # if a <= 0 or b <= 0 or c <= 0:
        #     raise ValueError("Los lados de un triángulo deben ser mayores a 0")
        # if a >= b + c or b >= a + c or c >= a + b:
        #     raise ValueError("Los lados de un triángulo deben cumplir con la desigualdad triangular")
        # self.a = a
        # self.b = b
        # self.c = c


if __name__ == '__main__':
    T = Triangle()
    T.get_values("a", 2.0, 3)