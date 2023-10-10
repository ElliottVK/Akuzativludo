'''
Main file for the educational game app.
'''
import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty, NumericProperty
import csv
from game import Word
class TitleScreen(Screen):
    '''
    Screen class for the title screen.
    '''
    pass
class LevelSelector(Screen):
    '''
    Screen class for the level selector.
    '''
    pass
class MainScene(Screen):
    '''
    Screen class for the main scene to play the game.
    '''
    def __init__(self, **kwargs):
        super(MainScene, self).__init__(**kwargs)
        self.game = Game()
        self.game.load_levels('game_data.csv')
    def on_enter(self):
        '''
        Event handler when entering the main scene.
        '''
        self.reset_scene()
    def reset_scene(self):
        '''
        Reset the scene to the initial state.
        '''
        self.clear_widgets()
        level = self.game.get_current_level()
        sentence = level['Sentence']
        missing_words = level['Missing Word'].split(',')
        word_order = level['Word Order'].split(',')
        layout = self.ids.word_layout
        layout.clear_widgets()
        for i, word in enumerate(sentence.split()):
            if str(i + 1) in word_order:
                draggable_word = Word(text=missing_words[word_order.index(str(i + 1))])
                draggable_word.order = int(word_order[word_order.index(str(i + 1))])
                layout.add_widget(draggable_word)
            else:
                layout.add_widget(Label(text=word))
    def check_answer(self):
        '''
        Check the answer and update the score.
        '''
        selected_words = [child for child in self.ids.word_layout.children if isinstance(child, Word)]
        is_correct = self.game.check_answer(selected_words)
        self.game.update_score(is_correct)
        if is_correct:
            self.show_popup('Correct!')
        else:
            self.show_popup('Incorrect!')
    def show_popup(self, message):
        '''
        Show a popup message.
        '''
        popup = Popup(title='Result', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()
    def next_level(self):
        '''
        Move to the next level or go back to the level selector.
        '''
        if self.game.current_level < len(self.game.levels) - 1:
            self.game.next_level()
            self.reset_scene()
        else:
            self.manager.current = 'level_selector'
class CreditsScene(Screen):
    '''
    Screen class for the credits scene.
    '''
    def get_credits(self):
        '''
        Get the credits from the text file.
        '''
        with open('credits.txt', 'r') as file:
            return file.read()
class WindowManager(ScreenManager):
    '''
    Screen manager class to manage different screens.
    '''
    pass
class AccusativeGameApp(App):
    '''
    Main app class for the educational game.
    '''
    def build(self):
        return WindowManager()
if __name__ == '__main__':
    AccusativeGameApp().run()