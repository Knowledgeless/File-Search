import os, sys, getpass

class FileSearch:
	def __init__(self):	
		self.os_name = sys.platform

	def getValue(self, user):
		file_name = user
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
		else:
			pass


if __name__ == "__main__":

	user = input("Your file name or extention: ")
	obj = FileSearch()
	obj.getValue(user)