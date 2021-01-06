from Exceptions import FieldCantAddShipException, FieldUsedPointException
from Dot import Dot
from Ship import Ship
from random import randint


class Field:

    def __init__(self, size, ships):

        self.size = size

        self._field = self.gen_field()
        self.hidden_field = self.gen_field()

        self.occupied_points = []
        self._ships = []

        self.neighbors = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        )

        self.needed_ships = dict(ships)
        self.needed_ships_copy = dict(self.needed_ships)

    def gen_field(self):

        field = []

        for i in range(self.size+1):
            field.append([])

        field[0].append(' ')

        for i in range(1, self.size+1):

            field[0].append(str(i))
            field[i].append(str(i))

            for k in range(self.size):
                field[i].append('O')

        return field

    def gen_ships(self):

        self.__init__(self.size, self.needed_ships_copy)

        for i in list(self.needed_ships.keys()):

            ship_len = int(i)

            attempts = 0

            while self.needed_ships[i] > 0:

                attempts += 1
                if attempts > 100:
                    self.__init__(self.size, self.needed_ships_copy)
                    return

                position = bool(randint(0, 1))

                if position:

                    x1 = x2 = randint(1, 6)

                    y1 = randint(1, self.size-ship_len)
                    y2 = y1 + ship_len - 1

                else:

                    y1 = y2 = randint(1, 6)

                    x1 = randint(1, self.size-ship_len)
                    x2 = x1 + ship_len - 1

                try:

                    ship = Ship((x1, y1), (x2, y2))

                    self.add_ship(ship)

                    self.needed_ships[i] -= 1

                except FieldCantAddShipException:
                    pass

    def add_ship(self, ship):

        try:
            for dot in ship.dots:

                if not self.check_neighbors(dot):
                    raise FieldCantAddShipException

            for dot in ship.dots:
                self._field[dot.x][dot.y] = '■'

            self.occupied_points += [i for i in ship.dots]
            self._ships.append(ship)

        except IndexError:
            raise FieldCantAddShipException

    def check_neighbors(self, dot):

        for dx, dy in self.neighbors:

            neighbor_dot = Dot(dot.x+dx, dot.y+dy)

            if neighbor_dot in self.occupied_points:
                return False

        return True

    def print_contour(self, ship):

        for dot in ship.dots:

            for dx, dy in self.neighbors:

                try:
                    if self._field[dot.x+dx][dot.y+dy] == 'O':
                        self._field[dot.x+dx][dot.y+dy] = '.'
                        self.hidden_field[dot.x+dx][dot.y+dy] = '.'

                except IndexError:
                    pass

    def attacked(self, dot):

        try:
            self._field[dot.x][dot.y]

        except IndexError:
            print('Input correct values')
            print('-'*29)
            return None

        if self._field[dot.x][dot.y] == 'O':

            self._field[dot.x][dot.y] = '.'
            self.hidden_field[dot.x][dot.y] = '.'

            print('Miss')
            print('-'*29)

            return True

        elif self._field[dot.x][dot.y] == '■':

            for ship in self._ships:

                if dot in ship.dots:

                    self._field[dot.x][dot.y] = 'X'
                    self.hidden_field[dot.x][dot.y] = 'X'
                    ship.health -= 1

                    if ship.health == 0:

                        self.print_contour(ship)
                        self._ships.remove(ship)

                        print('Ship defeated!')
                        print('-'*29)

                    else:
                        print('Hit!')
                        print('-'*29)

                    return False

        else:
            raise FieldUsedPointException

    def print_field(self):

        for i in self.field:

            for k in i:

                print(' ' + k + ' |', end='')

            if i != self.field[-1]:
                print('\n')

        print()
        print('-'*29)

    @property
    def field(self):
        return self._field

    @property
    def ships(self):
        return self._ships
