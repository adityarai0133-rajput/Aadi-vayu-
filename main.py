import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import requests

class AadiVayuMobile(App):
    def build(self):
        self.title = "KYXGO Aadi-Vayu Mobile"
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # Header
        self.layout.add_widget(Label(text="AADI-VAYU DISASTER ENGINE", font_size='20sp', color=(0, 1, 1, 1)))

        # City Input
        self.city_input = TextInput(text='', hint_text='Enter City Name...', multiline=False, size_hint_y=None, height=100)
        self.layout.add_widget(self.city_input)

        # Search Button
        self.btn = Button(text='ANALYZE RISK', size_hint_y=None, height=100, background_color=(0, 0.7, 0.9, 1))
        self.btn.bind(on_press=self.get_weather)
        self.layout.add_widget(self.btn)

        # Result Display
        self.result_label = Label(text="System Ready...", halign="center", valign="middle")
        self.layout.add_widget(self.result_label)

        return self.layout

    def get_weather(self, instance):
        city = self.city_input.text.strip()
        api_key = "3cf2fba56ff75639784c699d26b1654e" # Teri API Key
        
        if not city:
            self.result_label.text = "Error: City name is empty!"
            return

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()

            if response.status_code == 200:
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                risk = "LOW"
                if temp > 40 or "storm" in desc: risk = "HIGH"
                
                self.result_label.text = f"City: {city.upper()}\nTemp: {temp}°C\nStatus: {desc.upper()}\nRISK LEVEL: {risk}"
            else:
                self.result_label.text = "City Not Found!"
        except:
            self.result_label.text = "Network Error! Check Link."

if __name__ == "__main__":
    AadiVayuMobile().run()
