import os, sys, getpass
from queue import Empty
from string import ascii_uppercase as drives

class Banner:
    def banner(self):
        print('''\n\n
            888888 88 88     888888     .dP"Y8 888888    db    88""Yb  dP""b8 88  88 888888 88""Yb 
            88__   88 88     88__       `Ybo." 88__     dPYb   88__dP dP   `" 88  88 88__   88__dP 
            88""   88 88  .o 88""       o.`Y8b 88""    dP__Yb  88"Yb  Yb      888888 88""   88"Yb  
            88     88 88ood8 888888     8bodP' 888888 dP""""Yb 88  Yb  YboodP 88  88 888888 88  Yb
        \n\n''')
    

class FileSearch:
    def __init__(self, user):
        self.current_location = os.getcwd()
        self.location = []
        self.file_name = user
        self.files = []

    def getfiles(self, current_dir):
        for root, dirs, files in os.walk(current_dir):
            for file in files:
                if file == self.file_name or file.endswith(self.file_name.lower()):
                    self.location.append(os.path.join(root,file))

        return self.location
    
    def display(self, files):
        choice = input("Watch file(s) location now? (Y/n): ")
        if choice.lower() == "y":
            for file in files:
                print("\t{}".format(file))
        else:
            os.chdir(self.current_location)
            for i in files:
                with open("info.txt", "a") as name:
                    name.write("{}\n".format(i))
            print("Check 'info.txt' in your current folder.")

    def linux(self):
        try:
            username = getpass.getuser()
            os.chdir("/home/{}".format(username))
            current_dir = os.getcwd()
            self.files.append(self.getfiles(current_dir))
            if self.files is Empty:
                print("\n\tNothing Found..!\n\tTry agin with proper extension or file name.\n\n")
            else:
                self.display(self.files)
                
        except Exception as e:
            print("\n\tPlease Let Me Know The Error Message..!\n\n\tYour Error Message\n\t{}".format(e))

    def windows(self):
        try:
            existing_drives = ['%s:' % d for d in drives if os.path.exists('%s:' % d)]

            for i in existing_drives:
                os.chdir("{}\\".format(i))
                current_dir = os.getcwd()
                self.files.append(self.getfiles(current_dir))

            if self.files is Empty:
                print("\n\tNothing Found..!\n\tTry agin with proper extension or file name.\n\n")
            else:
                self.display(self.files)
        except Exception as e:
            print("\n\tPlease Let Me Know The Error Message..!\n\n\tYour Error Message\n\t{}".format(e))

if __name__ == "__main__":
    while True:
        obj = Banner()
        obj.banner()

        os_name = sys.platform		# Checking the OS name

        user = input("\tEnter your file name or extension: ")
        if user.lower() == "exit":
            exit()
        else:
            file_search = FileSearch(user)
            if os_name == "linux" or os_name=="unix":
                file_search.linux()
            elif os_name.startswith("win"):
                file_search.windows()
            else:
                print("\n\tLet Me Know Which 'Operation System' You Are Using..!\nYou are using: {}".format(os_name))
