import os

while True:
	userInput = input(">>> ")
	if userInput == "ls":
		print(os.listdir())
	
	elif userInput == "clear":
		os.system(userInput)

	elif userInput == "cwd":
		print(os.getcwd())

	elif userInput == "back":
		os.chdir("..")
		# print(os.getcwd())
	
	elif userInput == "cd":
		try:
			path = input("Which directory:")
			os.chdir(path)
		except OSError:
			path = input("Please enter the directory you want to change: ")
			os.chdir(path)

	elif userInput == "newdir":
			try:
				dirName = input("What is the directory name?: ")
				os.mkdir(dirName)
				print(f"Directory {dirName} created")
			except FileExistsError:
				dirName2 = input(f"There is already a directory named {dirName}. Try a different name: ")
				os.mkdir(dirName)
				print(f"Directory {dirName} created")

	elif userInput == "deldir":
		dirToRemove = input("Which directory do you want to remove?: ")
		os.rmdir(dirToRemove)
		print(f"Directory {dirToRemove} removed")

	elif userInput == "exit":
		exit()

	elif userInput == "rmfile":
		fileToBeRemoved = input("Which file do you want to remove?: ")
		os.remove(fileToBeRemoved)
		print(f"File {fileToBeRemoved} has been removed")

	elif userInput == "cfile":
		fileName = input("What's the file name?: ")
		file = open(fileName, "w+")
		file.close()

	elif userInput == "prev":
		fileToBePreviewed = input("Which file do you want to preview?: ")
		prevfile = open(fileToBePreviewed)
		showPrevFile = prevfile.read()
		print(showPrevFile)

	elif userInput == "rfile":
		fileToBeRenamed = input("Enter the name of the file you want to rename: ")
		fileToBeRenamedAs = input("Rename the file as: ")
		os.rename(fileToBeRenamed, fileToBeRenamedAs)
		print(f"File {fileToBeRenamed} has been renamed to {fileToBeRenamedAs}")

	else:
		print(f"COMMAND ERROR: {userInput} is not a command")
