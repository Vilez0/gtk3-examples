# use labels, buttons, and a box to arrange them
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.box = Gtk.Box()
        self.box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.label = Gtk.Label()
        self.label.set_label("Merhaba Gazi!")
        # https://docs.gtk.org/gtk3/method.Box.pack_start.html
        # self.box.pack_start(child, expand, fill, padding)
        self.box.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button()
        self.button.set_label("Tıkla!")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

    def on_button_clicked(self, widget):
        self.label.set_text("Merhabalar Gazi!")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()