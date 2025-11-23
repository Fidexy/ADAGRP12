class FixNum:
    """Representation of a signed fixed-point number.

    Attributes:
        prec (int): number of digits in the fractional part.
        s (int): sign (1 for positive, -1 for negative).
        a (int): integral part (absolute value).
        b (int): fractional part stored as integer with up to `prec` digits.
    """
    def __init__(self, prec, s=1, a=0, b=0):
        self.s = s
        self.a = a
        self.b = b
        self.prec = prec


    def input(self):
        """Read a fixed-point number from standard input.

        The expected input format is two separated integers: the integral
        part `a` and the fractional part `b`. For example for 12.34 (with
        prec=2) the user should enter: `12 34`.

        This method validates:
        - fractional part does not exceed the configured precision
        - negative signs are captured in `s` and the stored `a`/`b` are
          kept as absolute integers
        """
        # Prompt the user; split into integral and fractional parts
        self.a, self.b = input(f"Enter number a.b as [a] [b] (precision {self.prec}): ").split()
        if int(self.a) != 0 and int(self.b) < 0:
            raise Exception("Error: Negative fractional part with non-zero integral part.")

        # Ensure fractional part fits within the configured precision
        if len(str(abs(int(self.b)))) > self.prec:
            raise Exception(f"Error: Fractional part exceeds precision of {self.prec} digits.")

        # Determine sign: if either part is negative (or '-0') treat whole number as negative
        if int(self.a) < 0 or int(self.b) < 0 or self.a == '-0':
            self.s = -1
        else:
            self.s = 1

        # Store absolute integer components for internal representation
        self.a = abs(int(self.a))
        self.b = abs(int(self.b))

    def __str__(self):
        # Return a human-readable decimal string with zero-padded fractional part.
        if self.s == -1:
            return f"-{self.a}.{str(self.b).zfill(self.prec)}"
        else:
            return f"{self.a}.{str(self.b).zfill(self.prec)}"
    
    def __add__(self, num2):
        """Add two FixNum instances and return a new FixNum result.

        Addition is performed by converting both operands to scaled integers
        (multiplying by 10**prec), adding, then recovering the integral and
        fractional parts. The result preserves the configured precision.
        """
        # Scale to integer representation
        x = (float(self) * 10**self.prec)
        y = (float(num2) * 10**self.prec)
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
        # Convert this fixed-point number to a float respecting sign and precision.
        if self.s == -1:
            return float(f"{self.a}.{str(self.b).zfill(self.prec)}")*-1
        else:
            return float(f"{self.a}.{str(self.b).zfill(self.prec)}")
    
    def pow(self, num2):
        return(float(self)**float(num2))