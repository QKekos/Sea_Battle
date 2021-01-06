from Exceptions import FieldUsedPointException
from Input_settings import Settings
from Dot import Dot
from Player import Player
from Ai import Ai
from random import randint


class Game(Settings):

    def __init__(self):
        super().__init__()

        self.player = Player(self.size, self.ships)
        self.ai = Ai(self.size, self.ships)

        self.final_gen_ships()

        self.global_print()

        self.play()

    def final_gen_ships(self):

        if self.ships_placement_mode == 'auto':
            self.player.gen_ships()

        else:
            self.player.manual_place_ships()

        self.ai.gen_ships()

        while len(self.player.ships) == 0:
            self.player.gen_ships()

        while len(self.ai.ships) == 0:
            self.ai.gen_ships()

    def play(self):

        queue = True

        while True:

            if queue:

                change_queue = self.turn(self.player)

                if change_queue:
                    queue = not queue

            else:

                change_queue = self.turn(self.ai)

                if change_queue:
                    queue = not queue

            if change_queue is False or change_queue:
                self.global_print()

            if len(self.player.ships) == 0:
                print('Ai wins!')
                print('-'*29)
                break

            elif len(self.ai.ships) == 0:
                print('You win!')
                print('-'*29)
                break

    def turn(self, attacking_player):

        if attacking_player == self.ai:

            while True:

                x, y = randint(1, 6), randint(1, 6)

                try:
                    change_queue = self.player.attacked(Dot(x, y))
                    if change_queue is not None:
                        return change_queue

                except FieldUsedPointException:
                    pass

        else:

            coords = self.player.input_attack_coords()

            try:
                change_queue = self.ai.attacked(Dot(coords[0], coords[1]))

                if change_queue is not None:
                    return change_queue

            except FieldUsedPointException:
                print('You cant attack in the same place!')
                print('-'*29)

    def global_print(self):

        global_field = []

        for i in range(len(self.player.field)):

            global_field.append(
                self.player.field[i] + [' ' * 10] + self.ai.field[i]
            )

        for i in range(len(global_field) - 1):

            for k in global_field[i]:
                print('| ' + k, end=' ')

            print('|\n')

        for i in global_field[-1]:
            print('| ' + i, end=' ')

        print('|')

        print('-'*29)


if __name__ == '__main__':

    game = Game()
