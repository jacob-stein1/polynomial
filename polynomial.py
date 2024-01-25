class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_repr = repr(self.p1)
        p2_repr = repr(self.p2)

        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            p1_repr = "( " + p1_repr + " )"
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_repr = "( " + p2_repr + " )"
        return "( " + p1_repr + " / " + p2_repr + " )"

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_repr = repr(self.p1)
        p2_repr = repr(self.p2)

        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            p1_repr = "( " + p1_repr + " )"
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_repr = "( " + p2_repr + " )"
        return "( " + p1_repr + " - " + p2_repr + " )"

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

test1 = Mul(Add(Int(3), Int(2)), Int(4))
print(test1)  # (3 + 2) * 4

test2 = Sub(Mul(Add(Int(1), X()), Int(3)), Div(Int(4), Int(2)))
print(test2)  # (1 + X) * 3 - (4 / 2)

test3 = Div(Add(X(), Sub(Int(3), Mul(Int(1), Int(2)))), Add(Int(2), Int(4)))
print(test3)  # X + (3 - (1 * 2)) / (2 + 4)

test4 = Sub(Mul(Int(2), Add(Int(3), Int(4))), Div(Int(6), Add(Int(1), Int(1))))
print(test4)  # (2 * (3 + 4)) - (6 / (1 + 1))

test5 = Mul(Add(Mul(X(), Sub(Int(2), Int(1))), Div(Int(3), Add(Int(4), Int(1)))), Sub(Int(5), Int(2)))
print(test5)  # (X * (2 - 1) + (3 / (4 + 1))) * (5 - 2)
