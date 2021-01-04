from Exceptions import NonExistingShipError
from Dot import Dot



class Ship:

    def __init__(self, start_point, end_point=None):

        self.start_point = None
        self.end_point = None

        if end_point is None:
            self.start_point = self.end_point = start_point
            self._health = 1

        else:

            for i in range(2):

                if start_point[i] == end_point[i]:

                    if start_point[i-1] >= end_point[i-1]:

                        self.start_point = end_point
                        self.end_point = start_point
                        self._health = self.end_point[i-1] - self.start_point[i-1] + 1

                        break

                    else:

                        self.start_point = start_point
                        self.end_point = end_point
                        self._health = self.end_point[i-1] - self.start_point[i-1] + 1

                        break

        if self.start_point is None:
            raise NonExistingShipError

        self.dots = []
        self.create_dots_array()

    def create_dots_array(self):

        if self.start_point[0] == self.end_point[0]:  # Horizontal
            for i in range(self.start_point[1], self.end_point[1] + 1):
                self.dots.append(Dot(self.start_point[0], i))

        else:  # Vertical
            for i in range(self.start_point[0], (self.end_point[0]) + 1):
                self.dots.append(Dot(i, self.start_point[1]))

    def __repr__(self):
        return f'{self.health}: {self.dots}'

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if isinstance(value, int):

            if value >= 0:
                self._health = value

            else:
                raise ValueError("Health can't be less than zero")

        else:
            raise TypeError('Health can be only int')
