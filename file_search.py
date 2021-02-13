import os, sys, getpass

class FileSearch:
	def __init__(self):	
		self.os_name = sys.platform		# Checking the OS name


	def getValue(self, user):
		file_name = user
		try:
			if self.os_name == "linux":
				location = []
				username = getpass.getuser()
				os.chdir("/home/{}".format(username))
				cwd = os.getcwd()
				for root, dirs, files in os.walk(cwd):
					for file in files:
						if file == file_name or file.endswith(user.lower()):
							location.append(os.path.join(root, file))
						else:
							pass
				for i in location:
					print(i)

			elif self.os_name.startswith("win"):
				location = []
				dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
				drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

				for i in drives:
					os.chdir("{}\\".format(i))
					cwd = os.getcwd()
					for root, dirs, files in os.walk(cwd):
						for file in files:
							if file == file_name or file.endswith(user.lower()):
								location.append(os.path.join(root, file))
							else:
								pass
				print("\n")
				for i in location:
					print("\t{}".format(i))
				print("\n")
			else:
				print("""
					Let me know which Operating System you are using.
				""")

		except KeyboardInterrupt:
			print("Keyboard Interrupted")
		except Exception as e:
			print(e)

if __name__ == "__main__":
	
	user = input("Your file name or extention: ")
	obj = FileSearch()
	obj.getValue(user)
