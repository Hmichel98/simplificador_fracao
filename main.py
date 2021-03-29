import kivy 

kivy.require("1.9.0")


from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.boxlayout import BoxLayout 
from smp_function import simplificar

Builder.load_file("smp_app.kv")


class SmpLayout(BoxLayout):
    
    def mostrar_resultado(self):
        if self.numerador.text and self.denominador.text and not self.numerador.text.isalpha() and not self.denominador.text.isalpha():
            try:
                self.resultado.text = "[size=50][color=#1e3d59]" + simplificar(int(self.numerador.text), int(self.denominador.text))
            except:
                pass
        else:
            self.resultado.text = "[size=32][color=#1e3d59]Preencha os dois campos\n e/ou utilize apenas números"


class SmpApp(App):
    def build(self):
        return SmpLayout() 


if __name__=="__main__":
    SmpApp().run()