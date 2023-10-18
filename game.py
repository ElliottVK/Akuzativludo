from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.behaviors import DragBehavior
from kivy.uix.image import Image
from kivy.clock import Clock

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


class GameApp(App):
    
    def build(self):
        self.load_data()
        self.root = FloatLayout()
        self.display_sentence()
        return self.root

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
            drop_areas_layout.add_widget(drop_area)

            noun_options_layout = BoxLayout(orientation="vertical", size_hint=(0.2, 0.2),
                                           pos_hint={"x": 0.1 + (0.25 * index), "bottom": 0.1})
            drop_areas_layout.add_widget(noun_options_layout)
            for option in noun_data["word_options"]:
                btn = DraggableButton(text=option, size_hint_y=None, height=50)
                noun_options_layout.add_widget(btn)

    def on_option_select(self, instance):
        # Logic when an option is selected
        pass

    def check_answers(self):
        # Logic to check the answers
        pass


# Running the app
# GameApp().run()  # Commenting out the run command to prevent execution in this environment. Uncomment it to run the app.

car_images = ['00_car.png', '02_car.png', '04_car.png']

class AnimatedCar(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.source = car_images[self.index]
        Clock.schedule_interval(self.update, 0.2)  # Change the image every 0.2 seconds

    def update(self, *args):
        self.index = (self.index + 1) % len(car_images)
        self.source = car_images[self.index]

class YourApp(App):
    def build(self):
        return AnimatedCar()
