from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.behaviors import DragBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
import json
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

#scenes and scene managers
# Main Menu Screen
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        play_button = Button(text="Ludu", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        play_button.bind(on_press=self.go_to_level_selection)
        layout.add_widget(play_button)
        self.add_widget(layout)

    def go_to_level_selection(self, *args):
        self.manager.current = 'level_selection'

# Level Selection Screen
class LevelSelection(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # This is just a placeholder for now
        label = Label(text="Level Selection - Placeholder")
        layout.add_widget(label)
        self.add_widget(layout)
        
        # Add spots for each level
        for i in range(5):
            btn = Button(background_color=(0, 1, 0, 1))  # Green for Level 1
            layout.add_widget(btn)
        
        for i in range(4):
            btn = Button(background_color=(1, 1, 0, 1))  # Yellow for Level 2
            layout.add_widget(btn)
        
        for i in range(3):
            btn = Button(background_color=(1, 0.5, 0, 1))  # Orange for Level 3
            layout.add_widget(btn)

        self.add_widget(layout)


    class AnimatedCar(Image):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.index = 0
            self.source = car_images[self.index]
            Clock.schedule_interval(self.update, 0.2)  # Change the image every 0.2 seconds

        def update(self, *args):
            self.index = (self.index + 1) % len(car_images)
            self.source = car_images[self.index]




        def load_data(self):
            with open("parsed_data_output.json", "r") as f:
                self.data = json.load(f)
            self.current_data = self.data[0]
        
        def display_sentence(self):
            sentence = self.current_data["sentence"]
            for noun_data in self.current_data["noun_data"]:
                noun = noun_data["correct_noun"].rstrip("onjn")
                sentence = sentence.replace(noun, "_" * len(noun), 1)

            self.sentence_label = Label(text=sentence, size_hint=(0.9, 0.2), pos_hint={"x": 0.05, "top": 1})
            self.root.add_widget(self.sentence_label)
            
            drop_areas_layout = RelativeLayout(size_hint=(0.9, 0.6), pos_hint={"x": 0.05, "y": 0.2})
            self.root.add_widget(drop_areas_layout)
            noun_count = len(self.current_data["noun_data"])
            
            for index, noun_data in enumerate(self.current_data["noun_data"]):
                drop_area = Button(
                    text=str(index + 1),
                    size_hint=(0.2, 0.2),
                    pos_hint={"x": 0.1 + (0.25 * index), "center_y": 0.5},
                    background_color=(0, 0.6, 0, 1),  # Esperanto green
                )


        def on_option_select(self, instance):
            # Logic when an option is selected
            pass

        def check_answers(self):
            # Logic to check the answers
            pass

# Create the screen manager
class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainMenu(name="main_menu"))
        self.add_widget(LevelSelection(name="level_selection"))
        self.add_widget(MainMenu(name="main_menu"))

class Gameplay(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            # Add gameplay elements
        self.add_widget(Button(text='Back to Level Selection', on_press=self.back_to_levels))
        
    def back_to_levels(self, instance):
        self.manager.current = 'level_selection'


car_images = ['00_car.png', '02_car.png', '04_car.png']

# Define the draggable button
class DraggableButton(DragBehavior, Button):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.opacity = 0.5
        return super(DraggableButton, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.opacity = 1
        return super(DraggableButton, self).on_touch_up(touch)

def change_screen(self, instance):
    self.manager.current = "name_of_the_next_screen"

class AkuzativoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name="main_menu"))
        sm.add_widget(LevelSelection(name="level_selection"))
        sm.add_widget(Gameplay(name="gameplay"))
        return sm

# This is the main entry point of the app
if __name__ == "__main__":
    AkuzativoApp().run()
