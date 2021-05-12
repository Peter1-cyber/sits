# Создание и запуск приложения, программирование интерфейса экранов и действий на них

# Здесь должен быть твой код


# Здесь должен быть твой код
from scrollLabel import *
from kivy.uix.scrollview import ScrollView
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import *
from ruffier import *
from kivy.clock import Clock
from seconds import Seconds
from sits import Sits
from runner import *


age = 7
p1 = 0
p2 = 0
p3 = 0
name = ''
def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

def get_result():
    res = test(p1, p2, p3, age)
    return name + '\n' + res[0] + '\n' + res[1]

class MainScreen(Screen):
    def __init__(self, name = 'main', **kwargs):
        super().__init__(name=name, **kwargs)
        self.text = ScrollLabel(instruction)
        self.a1 = TextInput(multiline = False)
        self.a2 = TextInput(multiline = False)
        self.name1 = Label(text = 'Введите ваше имя: ', halign = 'right') 
        self.age = Label(text = 'Введите ваш возраст: ', halign = 'right')
        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

        self.wasd1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.wasd1.add_widget(self.name1)
        self.wasd1.add_widget(self.a1)
        self.wasd2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.wasd2.add_widget(self.age)
        self.wasd2.add_widget(self.a2)
        self.btn.on_press = self.next

        box1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        box1.add_widget(self.text)
        box1.add_widget(self.wasd1)
        box1.add_widget(self.wasd2)
        box1.add_widget(self.btn)

        self.add_widget(box1)


    def next(self):
        global age, name
        name = self.name1.text + ' ' + self.a1.text
        age = check_int(self.a2.text)
        if age == False or age < 7:
            age = 7
            self.a2.text = str(age)
        else:
            self.manager.current = 'first'


class FirstScreen(Screen):
    def __init__(self, name = 'first', **kwargs):
        super().__init__(name=name, **kwargs)
        self.nextscreen = False
        self.label_second = Seconds(15)
        self.label_second.bind(done = self.finish)

        self.text = ScrollLabel(instruction1)
        self.a1 = TextInput(multiline = False)
        self.a1.set_disabled(True)

        self.name1 = Label(text = 'Введите результат: ', halign = 'right') 
        self.btn = Button(text='Запустить таймер', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.wasd1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.wasd1.add_widget(self.name1)
        self.wasd1.add_widget(self.a1)

        box1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        box1.add_widget(self.text)
        box1.add_widget(self.label_second)
        box1.add_widget(self.wasd1)
        box1.add_widget(self.btn)

        self.add_widget(box1)

    def finish(self, *args):
        self.a1.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.nextscreen = True
    


    def next(self):
        if not self.nextscreen:
            self.btn.set_disabled(True)
            self.label_second.start()
        else:
            global p1
            p1 = check_int(self.a1.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.a1.text = str(p1)
            else:
                self.manager.current = 'second'





class SecondScreen(Screen):
    def __init__(self, name = 'second', **kwargs):
        super().__init__(name=name, **kwargs)
        self.nextscreen = False
        self.label_second = Sits(30)
        self.run = Runner(total = 30, steptime = 1.5, size_hint = (0.4, 1))
        self.run.bind(finish = self.finish)

        self.text = ScrollLabel(instruction2)
        self.btn = Button(text='Начать приседания', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        box1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        box1.add_widget(self.text)
        box1.add_widget(self.label_second)
        box1.add_widget(self.run)
        box1.add_widget(self.btn)
        self.add_widget(box1)
    def next(self):
        if not self.nextscreen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value = self.label_second.next)
        else:
            self.manager.current = 'third'



    def finish(self, *args):
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.nextscreen = True
    
class ThirdScreen(Screen):
    def __init__(self, name = 'third', **kwargs):
        super().__init__(name=name, **kwargs)
        self.nextscreen = False
        self.label_second = Seconds(60)
        self.label_second.bind(done = self.finish)
        self.text = ScrollLabel(instruction3)
        self.a1 = TextInput(multiline = False)
        self.a2 = TextInput(multiline = False)
        self.name1 = Label(text = 'Результат: ', halign = 'right') 
        self.age = Label(text = 'Результат после отдыха: ', halign = 'right')
        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.wasd1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.wasd1.add_widget(self.name1)
        self.wasd1.add_widget(self.a1)
        self.wasd2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.wasd2.add_widget(self.age)
        self.wasd2.add_widget(self.a2)
        box1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        box1.add_widget(self.text)
        box1.add_widget(self.label_second)
        box1.add_widget(self.wasd1)
        box1.add_widget(self.wasd2)
        box1.add_widget(self.btn)
        
        self.add_widget(box1)
    def next(self):
        if not self.nextscreen:
            self.btn.set_disabled(True)
            self.label_second.start()
        else:
            global p2, p3
            p2 = check_int(self.a1.text)
            p3 = check_int(self.a2.text)
            if p2 == False and p3 == False:
                p2 = 0
                self.a1.text = str(p2)
                p3 = 0
                self.a2.text = str(p3)
            elif p2 == False:
                p2 = 0
                self.a1.text = str(p2)
            elif p3 == False:
                p3 = 0
                self.a2.text = str(p3)
            else:
                self.manager.current = 'fourth'
    def finish(self, *args):
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.nextscreen = True
    

class FourthScreen(Screen):
    def __init__(self, name = 'fourth', **kwargs):
        super().__init__(name=name, **kwargs)
        self.text = ScrollLabel(instruction3)
        box1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        box1.add_widget(self.text)
        self.add_widget(box1)
        self.on_enter = self.before



    def before(self):
        self.text.set_text(get_result())


        
class ScrButton(Button):
    def __init__(self, screen, direction = 'right', goal = 'main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction=self.direction
        self.screen.manager.current = self.goal



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name= 'main'))
        sm.add_widget(FirstScreen(name= 'first'))
        sm.add_widget(SecondScreen(name= 'second'))
        sm.add_widget(ThirdScreen(name= 'third'))
        sm.add_widget(FourthScreen(name= 'fourth'))
        return sm




app = MyApp()
app.run()





# class MainScreen(Screen):
#     def __init__(self, name = 'main', **kwargs):
#         super().__init__(name=name, **kwargs)
#         box1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
#         box2 = BoxLayout()
#         text = Label(text= 'text')
#         box2.add_widget(text)
#         box1.add_widget(ScrButton(self, direction='right', goal = 'first', text = '1'))
#         box1.add_widget(ScrButton(self, direction='up', goal = 'second', text = '2'))
#         box1.add_widget(ScrButton(self, direction='left', goal = 'third', text = '3'))
#         box1.add_widget(ScrButton(self, direction='down', goal = 'fourth', text = '4'))
#         box2.add_widget(box1)
#         self.add_widget(box2)
# class FirstScreen(Screen):
#     def __init__(self, name = 'first', **kwargs):
#         super().__init__(name=name, **kwargs)
#         self.temp = BoxLayout()
#         self.temp.add_widget(ScrButton(self, text = 'qwe', size_hint=(.5, .4)))
#         self.temp.add_widget(ScrButton(self, text = 'wea', size_hint=(.5, .4)))
#         self.add_widget(self.temp)
# # , pos_hint={'center_x': 0.5, 'center_y': 0.5    }


        
# class SecondScreen(Screen):
#     def __init__(self, name = 'second', **kwargs):
#         super().__init__(name=name, **kwargs)
#         self.box1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
#         self.ti = TextInput(text='Hello', halign='right', focus=True, multiline=False)
#         self.text = Label(text= 'text')
#         self.box2 = BoxLayout()
#         self.key = Button(text = '2222', size_hint=(.5, .4))
#         self.box2.add_widget(self.key)
#         self.box2.add_widget(ScrButton(self, text = 'qwe', size_hint=(.5, .4)))
#         self.box1.add_widget(self.ti)
#         self.box1.add_widget(self.text)
#         self.box1.add_widget(self.box2)
#         self.add_widget(self.box1)
#         self.key.on_press=self.ChangeText



#     def ChangeText(self):
#         self.text.text=self.ti.text





# class ThirdScreen(Screen):
#     def __init__(self, name = 'third', **kwargs):
#         super().__init__(name=name, **kwargs)
# class FourthScreen(Screen):
#     def __init__(self, name = 'fourth', **kwargs):
#         super().__init__(name=name, **kwargs)
       











