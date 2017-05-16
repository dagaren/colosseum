import kivy

kivy.require('1.9.1')

from kivy.app import App
from board import Board

class ColosseumApp(App):
    def build(self):
        return Board()

if __name__ == '__main__':
    ColosseumApp().run()
    print(' => Normal termination of the program')