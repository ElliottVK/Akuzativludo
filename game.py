'''
Game logic file for the educational game app.
'''
import csv
from kivy.properties import NumericProperty
class Game:
    '''
    Class to handle game logic.
    '''
    def __init__(self):
        self.levels = []
        self.current_level = 0
        self.score = 0
    def load_levels(self, filename):
        '''
        Load levels from a CSV file.
        '''
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.levels.append(row)
    def get_current_level(self):
        '''
        Get the current level.
        '''
        return self.levels[self.current_level]
    def check_answer(self, selected_words):
        '''
        Check if the selected words are correct.
        '''
        level = self.get_current_level()
        missing_words = level['Missing Word'].split(',')
        word_order = level['Word Order'].split(',')
        if len(selected_words) != len(missing_words):
            return False
        for i, word in enumerate(selected_words):
            if word.text != missing_words[i] or word.order != int(word_order[i]):
                return False
        return True
    def update_score(self, is_correct):
        '''
        Update the score based on the correctness of the answer.
        '''
        if is_correct:
            self.score += 1
    def next_level(self):
        '''
        Move to the next level.
        '''
        self.current_level += 1
    def reset_game(self):
        '''
        Reset the game to the initial state.
        '''
        self.current_level = 0
        self.score = 0
class Word(Label):
    '''
    Class to represent a draggable word.
    '''
    order = NumericProperty()
    def __init__(self, **kwargs):
        super(Word, self).__init__(**kwargs)
        self.order = 0