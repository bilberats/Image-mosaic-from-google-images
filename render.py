from functions import resize_image, grayify, crop, closestimage,calculs_d
import os
import PIL.Image

def mosaic(folder_path,image_path,image_carreaux = 50,carreau_size = 50):

    image = PIL.Image.open(image_path)

    carreaux, shortest = calculs_d(folder_path)

    resized_image = resize_image(image,image_carreaux)
    width, height = resized_image.size


    #petite image en croped = carreau
    pixels = resized_image.getdata()


    mosaic = PIL.Image.new("RGB",(width*carreau_size,height*carreau_size),"black")

    for j in range(0,height*carreau_size,carreau_size):
        for i in range(0,width*carreau_size,carreau_size):
            pixel = pixels[((int(j/carreau_size))*width+int(i/carreau_size))]

            impath = PIL.Image.open(os.path.join(folder_path,closestimage(pixel, carreaux, shortest, folder_path)))
            carreau = crop(resize_image(impath,carreau_size))

            print((j*width/carreau_size)+i/carreau_size)
            mosaic.paste(carreau, (i,j))
    mosaic.show()
    if os.path.exists("last_image_color.jpg"):
        os.remove("last_image_color.jpg")
    mosaic.save("last_image_color.jpg")
