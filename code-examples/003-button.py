import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.button = Gtk.Button()
        self.button.set_label("Merhaba Gazi!")
        self.add(self.button)

win = MyWindow()
win.show_all()
Gtk.main()
