dat_path = "user_dat/"

# default values
preferences = {
    "show_notes" : True,
    "show_shell" : True,
    "show_variables" : True,
    "show_plot" : False
}

def load_preferences():
    try:
        file = open(dat_path + "preferences.txt", "r")
    except:
        print("No preferences saved")
        return

    for line in file.readlines():
        name, val = line.split()
        if val == "False":
            preferences[name] = False
        else:
            preferences[name] = True

    file.close()


def save_preferences():
    
    # open and read file
    file = open(dat_path + "preferences.txt", "w")
    for key in preferences.keys():
        file.write(f"{key} {preferences[key]}\n")
    file.close()

