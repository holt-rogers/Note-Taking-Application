import dearpygui.dearpygui as dpg
from preferences import *

# copy past stuff

dpg.create_context()
dpg.configure_app(docking=True, docking_space=True, load_init_file= dat_path + "custom_layout.ini") 
load_preferences()

# window ids for savinf dock layout

notes = dpg.generate_uuid()
shell = dpg.generate_uuid()
variables = dpg.generate_uuid()
plots = dpg.generate_uuid()

# main menu functtions
def show_window(sender, data):
    name = dpg.get_item_label(sender).lower()
    name = name.replace(" ", "_")
    preferences[name] = data
    if name == "show_notes":
        dpg.configure_item(item=notes, show=data)
    elif name == "show_shell":
        dpg.configure_item(item=shell, show=data)
    elif name == "show_variables":
        dpg.configure_item(item=variables, show=data)
    elif name == "show_plot":
        dpg.configure_item(item=plots, show=data)
    else:
        print(name, "window not recognized")


def save_layout():
    save_preferences()
    dpg.save_init_file(dat_path + "custom_layout.ini")


# main menu
with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Import")
        dpg.add_menu_item(label="Save")
        with dpg.menu(label="Save As"):
            dpg.add_menu_item(label=".txt")
            dpg.add_menu_item(label=".pdf")
            dpg.add_menu_item(label=".py")
    with dpg.menu(label = "Preferences"):
        dpg.add_menu_item(label = "Save window layout", callback = save_layout)
        dpg.add_checkbox(label="Show Notes", callback = show_window, default_value = preferences["show_notes"])
        dpg.add_checkbox(label="Show Shell", callback = show_window, default_value = preferences["show_shell"])
        dpg.add_checkbox(label="Show Variables", callback = show_window, default_value = preferences["show_variables"])
        dpg.add_checkbox(label="Show Plot", callback = show_window, default_value = preferences["show_plot"])
    
# written notes
with dpg.window(label = "Notes", tag = notes):
    with dpg.menu_bar():
        with dpg.menu(label="Tool"):
            dpg.add_menu_item(label="Draw")
            dpg.add_menu_item(label="Erase")
            dpg.add_menu_item(label="Line")
            dpg.add_menu_item(label="Rectange")
            dpg.add_menu_item(label="Circle")
            dpg.add_menu_item(label="Text")
            dpg.add_menu_item(label="Select")
            dpg.add_menu_item(label="Group Select")
        with dpg.menu(label = "Color"):
            dpg.add_color_picker(label="Color")

# shell (vancy calculator)
with dpg.window(label = "Shell", tag = shell, show = preferences["show_shell"]):
    dpg.add_text("Hello, world")

# show variables from shell (lowkey useless)
with dpg.window(label = "Variables", tag = variables, show = preferences["show_variables"]):
    pass

# plots created in shell
with dpg.window(label = "Ploting", tag = plots, show = preferences["show_plot"]):
    pass

    

dpg.create_viewport(title='Custom Title', width=1024, height=768, resizable=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

