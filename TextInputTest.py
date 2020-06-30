from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


# Kivy UI box
class AnswerInput(BoxLayout):
    pass


class TextInputTest(App):

    def build(self):
        return AnswerInput()


if __name__ == '__main__':
    TextInputTest().run()
