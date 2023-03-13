from kivymd.app import MDApp
from kivy.lang import Builder

gui = Builder.load_file()

class Myapp(MDApp):
    def build(self):
        return None

Myapp().run()