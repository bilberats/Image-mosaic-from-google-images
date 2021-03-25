from google_image_get_images import dlimages
from render import mosaic
import os



def main():
    rootpath = os.getcwd()+"\\"

    search = "livre d'enfant"
    folder_size = 100

    folder_path = dlimages(search,folder_size)

    image_name = "test.jpg"

    image_path = os.path.join(rootpath,image_name)
    
    #nombre de carreau
    image_carreaux = 50
    #taille du carreau
    carreau_size = 50

    mosaic(folder_path,image_path,image_carreaux,carreau_size)
    


main()