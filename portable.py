import os 
import shutil
from pyshortcuts import make_shortcut
def organizeProgram(source_folder,folder_destination):
    program_files = [f for f in os.listdir(source_folder) if f.endswith("Portable")]
    if program_files ==[]:
        print("No portable file found")
        return
    else:
        media_files= program_files[0]

    source_file_path = os.path.join(source_folder,media_files) 
    if media_files.endswith("Portable"):
        destination_file_path = os.path.join(folder_destination,media_files)
        print(destination_file_path)
        shutil.move(source_file_path,destination_file_path)
        print(f"Moved '{media_files}' to '{folder_destination}")
        os.chdir(destination_file_path)
        with open(f"{media_files}.ini","w") as file:
            file.write("DisableSplashScreen=true")
            print("Bootscreen Disabled")
        program_name = media_files.replace("Portable","").strip()
        program_icon = destination_file_path+"\App\Appinfo\\appicon.ico"
        executable_program = destination_file_path+"\\"+media_files+".exe"
        make_shortcut(script=executable_program,startmenu=True,name=program_name,executable=executable_program,icon=program_icon)
        print("Shortcut Created")
    else:
        print("No portable app found")

source_folder = 'D:\Downloads\\'
folder_destination= 'D:\Programs\\'
organizeProgram(source_folder,folder_destination)