#!/usr/bin/env python
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker, MDThemePicker, MDTimePicker
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (300, 500)

help_client = """

<DateScreen>:
    name:'Time'
    MDList:
        text: 'Good bye'
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "CHATS"
                        left_action_items: [['menu', lambda x: open_menu.set_state('open')]]
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Profile'
                                IconLeftWidget:
                                    icon: 'android'
                            OneLineIconListItem:
                                text: 'Profile 2'
                                IconLeftWidget:
                                    icon: 'android'
                            OneLineIconListItem:
                                text: 'Profile 3'
                                IconLeftWidget:
                                    icon: 'android'
                            OneLineIconListItem:
                                text: 'Profile 4'
                                IconLeftWidget:
                                    icon: 'android'
                            OneLineIconListItem:
                                text: 'Profile 5'
                                IconLeftWidget:
                                    icon: 'android'
                    
                                
                                
                          
                Widget:
                
        MDNavigationDrawer:
            id: open_menu
            BoxLayout:
                spacing: '8dp'
                padding: '8dp'
                orientation: 'vertical'
                Image:
                    source: 'istockphoto-1300845620-612x612.jpg'
                MDLabel:
                    text: 'User'
                    font_style: 'H5'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'User@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-profile-woman'
                        OneLineIconListItem:
                            text: 'Date'
                            on_release: app.click()
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Time'
                            on_release: app.time_pick()
                            IconLeftWidget:
                                icon: 'android'
                        OneLineIconListItem:
                            text: 'Theme'
                            on_release: app.change_theme()
                            IconLeftWidget:
                                icon: 'logout'
                    
                   
"""

class DateScreen(Screen):
    pass
sn = ScreenManager()
sn.add_widget(DateScreen(name='Time'))

class ChatApp(MDApp):
    def build(self):

        self.helper = Builder.load_string(help_client)

        return self.helper
    def click(self):
       picker = MDDatePicker()
       picker.open()

    def change_theme(self):
        themer = MDThemePicker()
        themer.open()
    def time_pick(self):
        time = MDTimePicker()
        time.open()

if __name__ == '__main__':
    ChatApp().run()