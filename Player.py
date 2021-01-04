from Exceptions import *
from Field import Field
from Ship import Ship


class Player(Field):

    def input_attack_coords(self):

        text = 'Input attack coordinates:\n'

        while True:

            input_string = input(text).split()
            print('-'*29)

            if len(input_string) != 2:
                text = 'Input 2 variables:\n'
                continue

            x, y = input_string

            if x.isdigit() and y.isdigit():
                return int(x), int(y)

            text = 'Input digits:\n'

    def input_ship_coords(self):

        text = 'Input start/end ship coordinates:\n'

        while True:

            input_string = input(text).split()
            print('-'*29)

            if len(input_string) != 2 and len(input_string) != 4:
                text = 'Input 2 or 4 variables:\n'
                continue

            if len(input_string) == 2:
                x, y = input_string

                if x.isdigit() and y.isdigit():
                    return (int(x), int(y))

            elif len(input_string) == 4:

                x1, y1, x2, y2 = input_string

                if (
                    x1.isdigit() and
                    y1.isdigit() and
                    x2.isdigit() and
                    y2.isdigit()
                ):
                    return (int(x1), int(y1)), (int(x2), int(y2))

            text = 'Input digits:\n'

    def manual_place_ships(self):

        while True:

            self.print_field()
            ship_coords = self.input_ship_coords()

            # Trying to create a ship

            try:
                if isinstance(ship_coords[0], tuple):
                    ship = Ship(ship_coords[0], ship_coords[1])

                else:
                    ship = Ship(ship_coords)

            except NonExistingShipError as error:
                print(error)
                continue

            # Checking is this ship needed

            if str(ship.health) in list(self.needed_ships.keys()):

                if self.needed_ships[str(ship.health)] <= 0:
                    print('Wrong ship size')
                    print('-'*29)
                    continue

            else:
                print('Wrong ship size')
                print('-'*29)
                continue

            # Trying to add ship on field

            try:
                self.add_ship(ship)
                self.needed_ships[str(ship.health)] -= 1

            except FieldCantAddShipException:
                print('You cant place ship here!')
                print('-'*29)
                continue

            self.print_field()

            if sum(list(self.needed_ships.values())) == 0:
                break
