import data_base
import data_export
import data_import
import view

def button_click():
    contact = view.get_value()
    data_export.init(contact)
    b = view.open_file(contact)
