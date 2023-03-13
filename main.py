from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
FloatLayout:
    MDRaisedButton:
        text: 'CLIQUE'


"""


class Myapp(MDApp):
    def build(self):
        return Builder.load_string(KV)

Myapp().run()