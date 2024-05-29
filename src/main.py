from textnode import TextNode
import os, shutil

def copy_tree(source, destination):

    if destination == "../public/":
        print("Deleting the 'public' directory")
        shutil.rmtree(destination)

    if not os.path.exists(destination):
        os.mkdir(destination)

    list_of_files = os.listdir(source)

    for entry in list_of_files:
        source_path = os.path.join(source, entry)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination)
            print(f'Copying {source_path} to {destination}')
        elif os.path.isdir(source_path):
            copy_tree(source_path,os.path.join(destination, entry))




def main():
    copy_tree('../static/', '../public/')

main()
