from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MorgageCalculator(MDApp):
    def build(self):
        return MDLabel(text="Hello, MorgageCalculator", halign="center")


MorgageCalculator().run()
