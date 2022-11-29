# delete folder which has subdirectories in it
import os
import json

# reading the file names from json file
with open('folder_names.json','r')as f:
    data = json.load(f)
    print(type(data))
    root = data['root']
    root = root.replace('\\','/')
    f_path = data['f_path']
    f_path = f_path.replace('\\','/')

# function to delete subdirectories inside folder
def dele(f_path1):

  # scanning the names of directories from folder

  for dir in os.scandir(f_path1):
    sub_directory_path = os.path.join(f_path,dir).replace('\\','/')

    # terminating condition if after deleting subdirectories it reaches root directory
    if sub_directory_path == root:
       exit()

    # if subdirectory is empty it code comes to know that it has reached the end of dir tree so it removes the directory
    # and calls the function again so that it can delete the remaining subdirectory which contained this directory.
    elif os.path.isdir(sub_directory_path) and os.listdir(sub_directory_path) == [] and sub_directory_path != root:
      print("end")
      os.rmdir(sub_directory_path)
      dele(f_path)

    # while traversing through the directories if it reaches some directory which is not empty then it calls the funtion
    # again by giving the same directory's path 
    elif os.path.isdir(sub_directory_path) and os.listdir(sub_directory_path) != [] and sub_directory_path!= root: 
      print("in")
      print(sub_directory_path)
      print(dir)
      dele(sub_directory_path)

    # if while traversing through the list of diretories and files if it encounters a file and path is not the root path 
    # then it removes that file and call the function again by pass actual main directory path.
    elif os.path.isfile(sub_directory_path) and sub_directory_path!= root:
      os.remove(sub_directory_path)
      base = '/{}'.format(os.path.basename(sub_directory_path))
      sub_directory_path = sub_directory_path.replace(base,"")
      print(sub_directory_path)
      dele(f_path)


dele(f_path)

# after removing all the files and folder inside the directory  it deletes the main directory
os.rmdir(f_path)

