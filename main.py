from gui import Gui
from tools.settings import Settings

def main():
    settings: Settings = Settings()
    try:
        settings_file_name_f = open("settingsFiles/settingsFileName.txt")
        settingsFileName_line:str=settings_file_name_f.readline()[0:-1]
        _, settingsFileName = settings.get_property_pair(settingsFileName_line)
        file_with_properties = open("settingsFiles/" + settingsFileName)
        settings.get_properties(file_with_properties)
    except Exception as exp:
        print(str(exp))
        return
    Gui(settings)


if __name__ == '__main__':
    main()