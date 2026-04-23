import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# use Glade to design the UI and load it here
builder = Gtk.Builder()
builder.add_from_file("main.glade")
window = builder.get_object("main_window")
window.show_all()
Gtk.main()