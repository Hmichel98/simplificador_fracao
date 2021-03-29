import kivy 

kivy.require("1.9.0")


from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.boxlayout import BoxLayout 
from smp_function import simplificar

Builder.load_file("smp_app.kv")


class SmpLayout(BoxLayout):
    
    def mostrar_resultado(self):
        if self.numerador.text and self.denominador.text:
            num, den = simplificar(int(self.numerador.text), int(self.denominador.text))
            self.resultado_num.text = "[size=112][color=#1e3d59]"+str(num)
            self.resultador_den.text = "[size=112][color=#1e3d59]"+str(den)
  


class SmpApp(App):
    def build(self):
        return SmpLayout() 


if __name__=="__main__":
    SmpApp().run()