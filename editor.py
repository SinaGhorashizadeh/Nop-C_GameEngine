from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('Editor.kv')

class Editor(Widget):
    pass

class EditorApp(App):
    def build(self):
        return Editor()

if __name__ == '__main__':
    EditorApp().run()