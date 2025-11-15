class FixNum:
    def __init__(self, prec, s=1,a=0, b=0):
        self.s = s
        self.a = a
        self.b = b
        self.prec = prec


    def input(self):
        self.a, self.b = input(f"Enter number a.b as [a] [b] (precision {self.prec}): ").split()
        if int(self.a) != 0 and int(self.b) < 0:
            raise Exception("Error: Negative fractional part with non-zero integral part.")
        if len(str(abs(int(self.b)))) > self.prec:
            raise Exception(f"Error: Fractional part exceeds precision of {self.prec} digits.")
        if int(self.a) < 0 or int(self.b) < 0 or self.a == '-0':
            self.s = -1
        else:
            self.s = 1
        self.a = abs(int(self.a))
        self.b = abs(int(self.b))

    def __str__(self):
        if self.s == -1:
            return f"-{self.a}.{str(self.b).zfill(self.prec)}"
        else:
            return f"{self.a}.{str(self.b).zfill(self.prec)}"
    
    def __add__(self, num2):
        x = (float(self) * 10**self.prec)*self.s
        y = (float(num2) * 10**self.prec)*num2.s
        result = x + y
        # print(x, y, result)
        if result < 0:
            self.s = -1
            result = abs(result)
        else:
            self.s = 1
        a = int(result // 10**self.prec)
        b = round(result % 10**self.prec)
        # print(a, b)         
        return FixNum(self.prec, self.s, a, b)
    
    
    def __float__(self):
        if self.s == -1:
            return float(f"-{self.a}.{str(self.b).zfill(self.prec)}")
        else:
            return float(f"{self.a}.{str(self.b).zfill(self.prec)}")
    
    def pow(self, num2):
        if int(self) == 0:
            raise Exception("Error: Fixed point number is zero")
        return(float(self)**float(num2))