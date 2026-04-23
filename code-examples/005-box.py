import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.box = Gtk.Box()
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.button1 = Gtk.Button()
        self.button1.set_label("Merhaba Gazi!")

        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.add(self.button1)

        self.button2 = Gtk.Button()
        self.button2.set_label("Merhaba GaziSiber!")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.add(self.button2)

        self.button3 = Gtk.Button()
        self.button3.set_label("Merhaba GaziSiber ÖzgürYazılım!")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.add(self.button3)

    def on_button1_clicked(self, widget):
        print("Merhabalar Gazi!")

    def on_button2_clicked(self, widget):
        print("Merhabalar GaziSiber!")

    def on_button3_clicked(self, widget):
        print("Merhabalar GaziSiber ÖzgürYazılım!")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
