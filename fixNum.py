class FixNum:
    def __init__(self, prec, a=0, b=0):
        # Store as a single integer: a * scale + b
        self.a = a
        self.b = b
        self.prec = prec


    def input(self):
        self.a, self.b = input(f"Enter number a.b as [a] [b] (precision {self.prec}): ").split()
        if int(self.a) != 0 and int(self.b) < 0:
            raise Exception("Error: Negative fractional part with non-zero integral part.")
        if len(str(abs(int(self.b)))) > self.prec:
            raise(f"Error: Fractional part exceeds precision of {self.prec} digits.")
    
    def __str__(self):
        return f"{self.a}.{str(self.b).zfill(self.prec)}"
    
    def __add__(self, num2):
        x = float(self) * 10**self.prec
        y = float(num2) * 10**self.prec
        result = x + y
        a = int(result // (10 ** self.prec))
        b = int(result % (10 ** self.prec))
        print(a, b)
        return FixNum(self.prec, a, b)
    
    def __float__(self):
        return float(f"{self.a}.{str(self.b).zfill(self.prec)}")
    
    def pow(self, num2):
        return(float(self)**float(num2))