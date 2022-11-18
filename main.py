import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=30
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=60,
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=80,
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        new_button = Button(
            text="О нас", pos_hint={"center_x": 0.5, "center_y": 0.5},  background_color = [180/255, 255/255, 255/255,1],
        )

        new_button.bind(on_press=self.on_newsol)
        main_layout.add_widget(new_button)
        return main_layout
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Очистка виджета с решением
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Не добавляйте два оператора подряд, рядом друг с другом
                return
            elif current == "" and button_text in self.operators:
            # Первый символ не может быть оператором
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
    def on_newsol (self,instance):
      # solution = str('Колька сделал!')
      #self.solution.text = str('Колька сделал!')
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text='Сделано для Семена Гаврилова!!!!(c)'))
        button = Button(text='Закрыть',background_color = [180/255, 103/255, 255/255,1])
        layout.add_widget(button)
        popup = Popup(title='Уведомление', content=layout)
        button.bind(on_press=popup.dismiss)
        popup.open()
if __name__ == '__main__':
    app = MainApp()
    app.run()
