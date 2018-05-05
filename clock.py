import time

from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from times import millis, sec, min,hour, convert
from times import dddd
from kivy.clock import Clock
import threading




class ClockApp(App):
    def __init__(self):
        super().__init__()
        self.millis = millis()
        self.seconds = sec()
        self.minutes = min()
        self.hours = hour()


    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.minutesbar = ProgressBar(value=60 * int(self.minutes) + int(self.seconds), max=3600)
        self.clocktext = Label(text=convert(self.hours, self.minutes, self.seconds), font_size='52sp')
        self.secsbar = ProgressBar(value=1000 * int(self.seconds) + self.millis, max=60000)
        self.buttonbar = BoxLayout(orientation='horizontal')
        self.ny = Button(text='New York', font_size='14sp')
        self.be = Button(text='Belgium', font_size='14sp')
        self.buttonbar.add_widget(self.ny)
        self.buttonbar.add_widget(self.be)

        layout.add_widget(self.secsbar)
        layout.add_widget(self.clocktext)
        layout.add_widget(self.minutesbar)
        layout.add_widget(self.buttonbar)
        return layout


    def update(self):
        while True:
            self.millis = millis()
            self.secsbar.value = 1000 * int(self.seconds) + self.millis
            if self.seconds is not sec():
                self.seconds = sec()
                if self.minutes is not min():
                    self.minutes = min()
                    if self.hours is not hour():
                        self.hours = hour()
                        self.clocktext.text = convert(self.hours, self.minutes, self.seconds)

                        self.minutesbar.value = 60 * int(self.minutes) + int(self.seconds)

    def on_start(self):
        t = threading.Thread(target=self.update)
        t.start()








if __name__ == '__main__':
    ClockApp().run()

