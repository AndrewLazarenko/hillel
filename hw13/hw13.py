# Доопрацюйте гру зі свого попереднього дз наступним чиноом:
# Обʼєкт гри може отримати тільки обʼєкти гласу Гравець
# Додайте до класу гри класметод, виклик якого виведе на екран інформацію про правила гри
# ("Гра [тут назва гри]. Гравцям потрібно обрати одну з фігур [тут перелік ігрових фігур з класу]
# і перемогти опонента")
from random import choice


class BasePlayer:
    def __init__(self, name=None):
        if name is None:
            self.name = input("Enter player's name: ")
        else:
            self.name = name

    def get_figure(self, options):
        return self._get_figure(options)

    def _get_figure(self, options):
        raise NotImplementedError


class HumanPlayer(BasePlayer):
    def _get_figure(self, options):
        names = [obj.name for obj in options]
        while True:
            user_input = input(f'Enter one of {names}: ')
            if user_input not in names:
                print('Wrong input')
                continue

            for obj in options:
                if obj.name == user_input:
                    return obj


class AIPlayer(BasePlayer):
    def _get_figure(self, options):
        ai_choice = choice(options)
        print(f'HINT {ai_choice.name}')
        return ai_choice


class BaseGameFigure:
    name = 'Unknown'

    def __eq__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        return type(self) == type(other)

    def __gt__(self, other):
        raise NotImplementedError


class Rock(BaseGameFigure):
    name = 'Rock'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, Scissors) or isinstance(other, Lizard):
            return True
        return False


class Scissors(BaseGameFigure):
    name = 'Scissors'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, Paper) or isinstance(other, Lizard):
            return True
        return False


class Paper(BaseGameFigure):
    name = 'Paper'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, Rock) or isinstance(other, Spock):
            return True
        return False


class Lizard(BaseGameFigure):
    name = 'Lizard'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, Spock) or isinstance(other, Paper):
            return True
        return False


class Spock(BaseGameFigure):
    name = 'Spock'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if isinstance(other, Scissors) or isinstance(other, Rock):
            return True
        return False


class RSPGame:
    game_name = 'Rock Scissors Paper Lizard Spock'
    rules = [Scissors(), Paper(), Rock(), Lizard(), Spock()]

    def __init__(self, player1, player2):
        if not isinstance(player1, BasePlayer) or not isinstance(player2, BasePlayer):
            raise ValueError("Both players must be instances of BasePlayer or its subclasses.")
        self.player1 = player1
        self.player2 = player2

    def _play(self):
        while True:
            f1 = self.player1.get_figure(self.rules)
            f2 = self.player2.get_figure(self.rules)

            if f1 == f2:
                print('Tie! Players chose the same figure, playing again...')
            elif f1 > f2:
                print(f'Player {self.player1.name} defeated {self.player2.name} with {f1.name}!')
                break
            else:
                print(f'Player {self.player2.name} defeated {self.player1.name} with {f2.name}!')
                break

    def play(self):
        print(f'{self.game_name} started')
        self._play()

    @classmethod
    def display_rules(cls):
        pieces_names = ', '.join([piece.name for piece in cls.rules])
        print(f"Game {cls.game_name}. Players need to choose one of the pieces [{pieces_names}] and defeat their opponent")

# Example usage:
ai_player = AIPlayer(name="AI Player")
human_player = HumanPlayer()

game = RSPGame(ai_player, human_player)
game.display_rules()
game.play()