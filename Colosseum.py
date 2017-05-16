import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label

class ColosseumApp(App):
    def build(self):
        return Label(text = 'Colosseum')

if __name__ == '__main__':
    ColosseumApp().run()
    print(' => Normal termination of the program')