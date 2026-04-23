import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.button1 = Gtk.Button()
        self.button1.set_label("Merhaba Gazi!")

        self.button1.connect("clicked", self.on_button1_clicked)
        # https://docs.gtk.org/gtk3/method.Grid.attach.html
        # self.grid.attach(widget, column, row, width, height)
        self.grid.attach(self.button1, 0, 0, 1, 1)

        self.button2 = Gtk.Button()
        self.button2.set_label("Merhaba GaziSiber!")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.grid.attach(self.button2, 1, 1, 1, 1)

        self.button3 = Gtk.Button()
        self.button3.set_label("Merhaba GaziSiber ÖzgürYazılım!")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.grid.attach(self.button3, 2, 2, 1, 1)


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
