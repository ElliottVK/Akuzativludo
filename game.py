
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

# Data
parsed_data = [{
    "difficulty": "simple",
    "correct_index": 1,
    "sentence": "La pomo estas sur la ^.",
    "word_options": ["tablo", "tablon"]
}, {
    "difficulty": "simple",
    "correct_index": 1,
    "sentence": "Mi donis la ^ al mia amiko.",
    "word_options": ["libro", "libron"]
}, {
    "difficulty": "simple",
    "correct_index": 1,
    "sentence": "La ^ estas granda kaj bela.",
    "word_options": ["floro", "floron"]
}]

# Answer Drop Area
class AnswerDropArea(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Esperanto Green color
            Color(0, 0.56, 0.33, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

# Sentence Button
class SentenceButton(Button):
    def __init__(self, sentence, word_height, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.original_text = sentence
        self.text = sentence.replace('^', '_____')
        self.background_color = (0, 0, 0, 0)  # Transparent background
        self.width = self.texture_size[0]
        self.height = word_height * 3
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.75}

    def set_word(self, word):
        self.text = self.original_text.replace('^', word)

# Draggable Word Block
class DraggableWordBlock(Widget):
    def __init__(self, word, width, height, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width = width
        self.height = height
        with self.canvas:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(pos=self.pos, size=self.size)
            Color(0, 0, 0, 1)  # Black text
            self.label = Label(text=word)
            self.label.texture_update()
            self.texture = self.label.texture
            self.label.pos = self.pos
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.label.pos = self.pos

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.touch_diff = (touch.x - self.pos[0], touch.y - self.pos[1])
            return True
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.pos = (touch.x - self.touch_diff[0], touch.y - self.touch_diff[1])
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            # Check for collision with the answer drop area
            if self.collide_widget(self.parent.drop_area):
                self.parent.handle_word_drop(self)
            return True
        return super().on_touch_up(touch)

# Main Game Layout
class GameLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Block dimensions
        self.block_width = 100
        self.block_height = 40

        # Get the first sentence from parsed_data
        self.index = 0
        self.correct_word = parsed_data[self.index]['word_options'][parsed_data[self.index]['correct_index']-1]
        
        self.sentence_button = SentenceButton(parsed_data[self.index]['sentence'], self.block_height)
        self.add_widget(self.sentence_button)

        # Answer drop area
        self.drop_area = AnswerDropArea(size=(150, 150), size_hint=(None, None))
        self.drop_area.pos_hint = {'center_x': 0.5, 'center_y': 0.6}
        self.add_widget(self.drop_area)

        self.load_options()

    def load_options(self):
        for word in parsed_data[self.index]['word_options']:
            btn = DraggableWordBlock(word, self.block_width, self.block_height)
            self.add_widget(btn)


    def handle_word_drop(self, word_block):
        # Remove the word block from the screen
        self.remove_widget(word_block)
        
        # Check if the word is correct
        if word_block.text == self.correct_word:
            self.sentence_button.set_word(word_block.text)
            self.display_message("Ĝusta respondo ✔️", font_name="NotoColorEmoji.ttf")
        else:
            self.display_message("Malĝusta respondo ❌", font_name="NotoColorEmoji.ttf")

    def display_message(self, message, font_name=""):
        self.clear_widgets()
        msg_label = Label(text=message, font_size=20, font_name=font_name)
        self.add_widget(msg_label)
        continue_btn = Button(text="Click to continue", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        continue_btn.bind(on_press=self.load_next_sentence)
        self.add_widget(continue_btn)

    def load_next_sentence(self, *args):
        self.index += 1
        if self.index < len(parsed_data):
            self.clear_widgets()
            # Update the sentence and options
            self.correct_word = parsed_data[self.index]['word_options'][parsed_data[self.index]['correct_index']-1]
            self.sentence_button = SentenceButton(parsed_data[self.index]['sentence'], self.block_height)
            self.add_widget(self.sentence_button)
            
            # Answer drop area
            self.drop_area = AnswerDropArea(size=(150, 150), size_hint=(None, None))
            self.drop_area.pos_hint = {'center_x': 0.5, 'center_y': 0.6}
            self.add_widget(self.drop_area)

            self.load_options()
        else:
            # Game over
            self.clear_widgets()
            self.add_widget(Label(text="Congratulations! You've completed the game!"))

class GameApp(App):
    def build(self):
        return GameLayout()

if __name__ == '__main__':
    GameApp().run()
