import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Create a new window class that inherits from glade's Gtk.Window


class MyWindow:
    def __init__(self):
        super().__init__()

        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        self.builder.connect_signals(self)


        self.window = self.builder.get_object("main_window")
        self.button = self.builder.get_object("my_button")

    def benim_butonun_fonksiyonu(self, widget):
        print("Merhaba Gazi!")


Application = MyWindow()
Application.window.show_all()
Gtk.main()
