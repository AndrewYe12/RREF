
def fraction(self):
    for x in range(len(self.matrix)):
        for y in range(len(self.matrix[0])):
            self.matrix[x][y] = str(frac(str(self.matrix[x][y])).numerator) + '/' + str(frac(str(self.matrix[x][y])).denominator)
    return self.matrix