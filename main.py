from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = False
        self.last_button = None

        self.grid = GridLayout(cols=4, padding=10, spacing=10, row_default_height=100, col_default_width=100)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.grid.bind(minimum_width=self.grid.setter('width'))

        self.result = TextInput(
            readonly=True, halign='right', font_size=32, background_color='white'
        )
        self.grid.add_widget(self.result)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+',
            '='
        ]

        for button in buttons:
            btn = Button(
                text=button, font_size=32,
                background_color='gray', color='black',
                border=(20, 20, 20, 20), background_normal=''
            )
            btn.bind(on_release=self.on_button_press)
            self.grid.add_widget(btn)

        return self.grid

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        elif button_text == '=':
            try:
                self.result.text = str(eval(self.result.text))
            except Exception:
                self.result.text = 'Error'
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                self.result.text += button_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

if __name__ == '__main__':
    CalculatorApp().run()
