class Rectangle:
    '''A class defining a rectangle entity'''
    top = 0
    left = 0
    bottom = 1
    right = 1
    name = ''

    def __init__(self, tp: int, lt: int, bt: int, rt: int):
        self.top = tp
        self.left = lt
        self.bottom =bt
        self.right = rt

    def coords(self):
        return [(self.top, self.left), (self.bottom, self.right)]

    def area(self):
        return ((self.bottom - self.top) * (self.right - self.left))
