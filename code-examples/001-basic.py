import gi #GObject Introspection, allows us to use libraries like GTK in Python

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = Gtk.Window()
win.show_all()
Gtk.main()
