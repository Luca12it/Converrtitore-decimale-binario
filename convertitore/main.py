from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ConverterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.label = Label(text="Inserisci un numero decimale:", font_size=20)
        self.add_widget(self.label)

        self.input = TextInput(hint_text="Numero decimale", multiline=False, input_filter="int")
        self.add_widget(self.input)

        self.button = Button(text="Converti in binario", size_hint=(1, 0.3))
        self.button.bind(on_press=self.converti)
        self.add_widget(self.button)

        self.result = Label(text="", font_size=18)
        self.add_widget(self.result)

    def converti(self, instance):
        try:
            numero = int(self.input.text)
            self.result.text = f"Binario: {bin(numero)[2:]}"
        except ValueError:
            self.result.text = "Inserisci un numero valido!"


class ConverterApp(App):
    def build(self):
        return ConverterLayout()


if __name__ == "__main__":
    ConverterApp().run()