from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.07, 0.1, 1)

class NazzFiberMonitor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20
        self.add_widget(Label(text="NAZZ FIBER INTERNET", font_size='24sp', bold=True))
        self.lbl_pub_ip = Label(text="🌐 Public IP: Fetching...")
        self.add_widget(self.lbl_pub_ip)

class MyApp(App):
    def build(self):
        return NazzFiberMonitor()

if __name__ == '__main__':
    MyApp().run()
