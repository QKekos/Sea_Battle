from Exceptions import NonExistingShipError
from Dot import Dot


class Ship:

    def __init__(self, start_point, end_point=None):

        if not isinstance(start_point, Dot):
            if isinstance(start_point, tuple):
                start_point = Dot(start_point[0], start_point[1])

        if end_point is not None and not isinstance(end_point, Dot):
            if isinstance(end_point, tuple):
                end_point = Dot(end_point[0], end_point[1])

        if end_point is None:
            self.start_point = self.end_point = start_point
            self._health = 1

        else:
            self.set_minmax_dots(start_point, end_point)

        self.dots = []
        self.create_dots_array()

    def set_minmax_dots(self, first_dot, second_dot):

        if first_dot.x == second_dot.x:

            if first_dot.y >= second_dot.y:
                
                self.start_point = Dot(first_dot.x, second_dot.y)
                self.end_point = Dot(first_dot.x, first_dot.y)

                self.health = first_dot.y - second_dot.y + 1
                return

            else:
                
                self.start_point = Dot(first_dot.x, first_dot.y)
                self.end_point = Dot(first_dot.x, second_dot.y)

                self.health = second_dot.y - first_dot.y + 1
                return

        elif first_dot.y == second_dot.y:

            if first_dot.x >= second_dot.x:
                
                self.start_point = Dot(second_dot.x, first_dot.y)
                self.end_point = Dot(first_dot.x, first_dot.y)

                self.health = first_dot.x - second_dot.x + 1
                return

            else:
                
                self.start_point = Dot(first_dot.x, first_dot.y)
                self.end_point = Dot(second_dot.x, first_dot.y)

                self.health = second_dot.x - first_dot.x + 1
                return

        raise NonExistingShipError

    def create_dots_array(self):

        if self.start_point.x == self.end_point.x:  # Horizontal
            for new_y in range(self.start_point.y, self.end_point.y + 1):
                self.dots.append(Dot(self.start_point.x, new_y))

        else:  # Vertical
            for new_x in range(self.start_point.x, self.end_point.x + 1):
                self.dots.append(Dot(new_x, self.start_point.y))

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
