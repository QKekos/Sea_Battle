
class Settings:

    def __init__(self):

        print('-'*29)

        def size_input():

            text = 'Input field size [6, 12]:\n'

            while True:

                size = input(text)
                print('-'*29)

                if size.isdigit():
                    size = int(size)

                else:
                    text = 'Input number:\n'
                    continue

                if size > 12:
                    text = 'Too big field, input correct value:\n'
                    continue

                elif size < 6:
                    text = 'Too small field, input correct value:\n'
                    continue

                return size

        def ships_input():

            text = 'Input manual/auto input ships:\n'

            while True:

                input_string = input(text)
                print('-'*29)

                if input_string not in ['manual', 'auto']:
                    text = 'Input correct value:\n'
                    continue

                else:
                    break

            if input_string == 'auto':
                return {'3': 1, '2': 2, '1': 4}

            # Manual input ships

            def max_possible_points():

                mult = (self.size-6)/10
                return int(self.size*(2+mult))-1

            def count_points():

                sum_ = 0

                for i in list(ships_dict.keys()):
                    sum_ += int(i)*ships_dict[i]

                return sum_

            ships_dict = {}

            max_possible_points = max_possible_points()

            text = 'Input ship size(max 4) and count, blank line for exit:\n'

            while True:

                input_string = input(text)
                print('-'*29)

                if input_string == '':
                    if len(ships_dict) > 0:
                        break

                    else:
                        text = 'Input at least 1 ship type:\n'
                        continue

                text = 'Input ship size(max 4) and count, blank line for exit:\n'

                input_string = input_string.split()

                if len(input_string) != 2:
                    text = 'Input correct values:\n'
                    continue

                key, value = input_string[0], input_string[1]

                if (
                    (key.isdigit() and 1 <= int(key) <= 4) and
                    value.isdigit()
                ):
                    value = int(value)
                    ships_dict[key] = value

                    if count_points() > max_possible_points:

                        print('Too many ships')
                        del ships_dict[key]

                else:
                    text = 'Input correct values:\n'
                    continue

            return ships_dict

        def ships_placement_mode_input():

            text = 'Input manual/auto ships placement mode:\n'

            while True:

                input_string = input(text)
                print('-'*29)

                if input_string not in ['manual', 'auto']:
                    text = 'Input correct value:\n'
                    continue

                else:
                    break

            return input_string

        self.size = size_input()
        self.ships = ships_input()
        self.ships_placement_mode = ships_placement_mode_input()
