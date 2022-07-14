
import kivy
from kivy.app import App
from kivy.uix.button import Button

#.kv file specifies layout while python file mainly does logic

class TestButton(Button):
    def super__init__(self,**kwargs):
        self.text= 'test',
        self.size_hint=(0.5,0.5),
        self.pos=("100,100")
        #pos is position in x and y dont need if using hsize hint,size hint is like the proportion of the parent class hieght and width refernces
class testApp(App):
    def build(self):
        return TestButton()

if __name__== '__main__':
    testApp().run()
