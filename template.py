import os


<<<<<<< HEAD
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


=======
dirs=[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
   "notebooks",
    "saved_models",
    "src"
]
for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open (os.path.join(dir_,".gitkeep"),"w") as f:
        pass

>>>>>>> 831c59e58ae32dcea4ff4a89bb665c201ef7dbd8
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]
<<<<<<< HEAD

for file_ in files:
    with open(file_, "w") as f:
        pass
=======
for file_ in files:
    with open(file_,"w") as f:
        pass
>>>>>>> 831c59e58ae32dcea4ff4a89bb665c201ef7dbd8
