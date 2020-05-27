
class Vector:

    def __init__(self, values):
        self.values = []
        if isinstance(values, list):
            self.values = values
        elif isinstance(values, int):
            for i in range(values):
                self.values.append(float(i))
        elif isinstance(values, tuple):
            for i in range(values[0], values[1]):
                self.values.append(float(i))
        self.size = len(self.values)

    def __add__(self, vect):
        if vect.size == self.size:
            return [x + y for x, y in zip(vect.values, self.values)]

    def __radd__(self, scal):
        return [x + scal for x in self.values]

    def __sub__(self, vect):
        if vect.size == self.size:
            return [x - y for x, y in zip(self.values, vect.values)]

    def __rsub__(self, scal):
        return[x - scal for x in self.values]

    def __truediv__(self, scal):
        return [x / scal for x in self.values]

    def __rtruediv__(self, scal):
        pass

    def __mul__(self, vect):
        if vect.size == self.size:
            return [x * y for x, y in zip(vect.values, self.values)]

    def __rmul__(self, scal):
        return [x * scal for x in self.values]

    def __str__(self):
        s = "Vector:" + str(self.values)
        return s

    def __repr__(self):
        s = "Vector:" + str(self.values) + "Size: " + self.size
        return s
