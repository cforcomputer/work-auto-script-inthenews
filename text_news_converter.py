import kivy
import main_format_run as input_format
import pkg_resources.py2_warn


from kivy.app import App

# The TextInput widget provides a
# box for editable plain text
from kivy.uix.textinput import TextInput

# BoxLayout arranges widgets in either
# in vertical fashion that
# is one on top of another or in
# horizontal fashion that is one after another.
from kivy.uix.boxlayout import BoxLayout

# Button for submitting the inthenews
from kivy.uix.button import Button

kivy.require('1.9.0')


class Newser(App):
    def build(self):
        box_window = BoxLayout(orientation='vertical')

        # Adding the text input
        text_box = TextInput(font_size=12,
                             size_hint_y=12,
                             height=50)

        with open("input.txt", "w+") as f:
            contents = f.read()
            text_box.text = contents

        # The format button gui
        btn = Button(text="Format",
                     font_size="20sp",
                     height=30)
        # The clear button gui
        btn_clear = Button(text="Clear",
                           font_size="15sp",
                           size_hint_y=None,
                           height=20)

        # The format button action when pressed
        def format_action(event):
            print("Button pressed - Formatting")
            try:
                input_format.run_formatter()
                text = open("output.txt", "r")
                text_box.text = text.read()
            except SyntaxError:
                print("Syntax error in main_format")

        # The text box action when typed in
        def on_text(instance, value):
            print('The widget', instance, 'has value:', value)
            text_box_saver = open("input.txt", "w")
            text_box_saver.write(value)

        # The clear button action when pressed
        def clear(instance):
            text_box_saver = open("input.txt", "w")
            text_output = open("output.txt", "w")
            text_output.truncate(0)  # clear output.txt
            text_box_saver.truncate(0)  # clear input.txt
            text_box.text = ''  # clear the text box in gui

        # Bind button to action
        # When button is clicked, run the callback and perform action
        # under def callback(event)
        btn.bind(on_press=format_action)
        # Update when new text is entered in the text box (perform text callback)
        text_box.bind(text=on_text)
        # Clear the text in the textbox and input.txt when pressed
        btn_clear.bind(on_press=clear)

        box_window.add_widget(btn)  # Adding button to text box
        box_window.add_widget(btn_clear)
        box_window.add_widget(text_box)  # Added Text input box

        return box_window


# Running the newser class
Newser().run()
