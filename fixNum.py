class FixNum:
    def __init__(self, a=0, b=0):
        # Store as a single integer: a.b
        from __main__ import prec
        self.a = a
        self.b = b
        self.prec = prec


    def input(self):
        self.a, self.b = input(f"Enter number a.b as [a] [b] (precision {self.prec}): ").split()
        if int(self.a) > 0 and int(self.b) < 0:
            print("Error: Negative fractional part with non-zero integral part.")
            Exception()
        
    
    def __str__(self):
        return f"{self.a}.{str(self.b).zfill(self.prec)}"
    
    def __add__(self, num2):
        a = int(self.a) + int(num2.a)
        b = int(self.b) + int(num2.b)
        if len(str(b)) > self.prec:
            a += b // (10 ** self.prec)
            print(b // (10 ** self.prec))
            b = b % (10 ** self.prec)
            print(b % (10 ** self.prec))
        return FixNum(a, b)
    
    def __float__(self):
        return float(f"{self.a}.{str(self.b).zfill(self.prec)}")
    
    def pow(self, num2):
        return(float(self)**float(num2))