# Limits Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from sympy import Limit, Symbol, S, diff, integrate, solve
import math

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared-Mathematics : Limits Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"                 
                
""")

#Menu
Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
                    
            Button:
                font_size: 75
                background_color: 1, 1, 0, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Limits Calculator"
                on_release:
                    app.root.current = "Limits"
                    root.manager.transition.direction = "left"
                    
            Button:
                font_size: 75
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Button:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.ksquaredmathematics.com/subscribe') 
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics "
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 1000
                width: 1000
                
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 50
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-Mathematics?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Limits Calculators v0.1"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")

#Limits
Builder.load_string("""
<Limits>
    id:Limits
    name:"Limits"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Limits Calculator"
                
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        range.text = ""
                        direction.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "lim:"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10              
            
            TextInput:
                id: range
                text: range.text
                hint_text: "x -> n:"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10, 10
                
            TextInput:
                id: direction
                text: direction.text
                hint_text: "direction: + or -"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 125
                padding: 10, 10
                input_filter: lambda text, from_undo: text[:1 - len(direction.text)]
            
            BoxLayout:
                cols: 2
                padding: 10
                spacing: 10
                size_hint: 1, None
                width: 300
                size_hint_y: None
                height: self.minimum_height
                
                Button:
                    text: "\u221E"  
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 1, 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release: 
                        range.text = "\u221E"
                        
                Button:
                    text: "-\u221E"  
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 1, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release: 
                        range.text = "-\u221E"
                    
            Button:
                id: steps
                text: "Limit"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1, 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets()
                    Limits.Limit(entry.text + "&" + range.text + "%" + direction.text)
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Limits(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Limits, self).__init__(**kwargs)

    layouts = []
    def Limit(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("~~~~~~~~~~~~~~~~~~~~")
        print("LIMIT")
        
        try:
            print()
            print("Entry",entry)
            
            amp = entry.find("&")
            
            perc = entry.find("%")
            
            func = entry[:amp]
            print("func: ",func)
            
            func = func.replace("^","**").replace("x","*x").replace("***","**")
            func = func.replace("sin","*sin").replace("cos","*cos").replace("tan","*tan").replace("sec","*sec").replace("csc","*csc").replace("cot","*cot")
            func = func.replace("e","*e").replace("s*ec","sec").replace("-*","-").replace("+*","+").replace("(*x","(x").replace("(*y","(y").replace("(*z","(z").replace("/*","/")
            print("func cleaned: ",func)
            
            if func[0] == "*":
                func = func[1:]
                print("func cleaned: ",func)
            
            limit = entry[amp+1:perc]
            print("limit: ",limit)
            
            direction = entry[perc+1:]
            print("direction",direction)
            
            if limit == "∞":
                print("TO + INFINITY AND BEYONDDDD")
                limit = S.Infinity
                print("Limit: ",limit)
                print("func: ",func)
                x = Symbol("x")
                
                L = Limit(func,x,limit,dir=str(direction))
                
                Answer = str(L.doit()).replace("AccumBounds","Range : ")
                
                print()
                print("Answer: ",Answer)
            elif limit == "-∞":
                print("TO - INFINITY AND BEYONDDDD")
                limit = S.NegativeInfinity
                print("Limit: ",limit)
                print("func: ",func)
                
                x = Symbol("x")
                L = Limit(func,x,limit,dir=direction)
                Answer = str(L.doit()).replace("AccumBounds","Range : ")
                print()
                print("Answer: ",Answer)
                
            else:
                print("func: ",func)
                x = Symbol("x")
                L = Limit(func,x,limit,dir=direction)
                Answer = str(L.doit()).replace("AccumBounds","Range : ")
                print()
                print("Answer: ",Answer)
                
                
            self.ids.list_of_steps.add_widget(Label(text= "The Limit of :" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Lim (x -> " + str(limit) + ") " + direction + " : " + str(func).replace("**","^") ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "=" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= str(Answer).replace("**","^") ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass            

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Limits(name="Limits"))
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   

class Limits_Calculator(App):
    def __init__(self, **kwargs):
        super(Limits_Calculator, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Limits_Calculator().run()
