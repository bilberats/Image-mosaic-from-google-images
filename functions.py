import os
import PIL.Image


#resize images with a given width
def resize_image(image,new_size):
    width, height = image.size

    #2 size if we have to keep the largest side
    if height >= width:
        ratio = height / width
        new_size2 = int(new_size*ratio)
        resized_image = image.resize((new_size, new_size2))
    else:
        ratio = width/height
        new_size2 = int(new_size*ratio)
        resized_image = image.resize((new_size2, new_size))


    return resized_image




#convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


#crop images into squares
def crop(image):
    width, height = image.size
    
    if width <= height:
        resize = int((height-width)/2)

        left = 0
        top = resize
        right = width
        bottom = height-resize

        croped = image.crop((left, top, right, bottom))
    else:
        resize = int((width-height)/2)

        left = resize
        top = 0
        right = width-resize
        bottom = height

        croped = image.crop((left, top, right, bottom))
    return croped


def closestimage(imagepixel,carreaux,shortest,rootpath):
    #carreaux is a list of paths for images/carreaux

    #imagepixel is the getdata()[0] of the pixel
    r,g,b= imagepixel[:3]
    rc = r**2
    gc = g**2
    bc = b**2

    #highest value of d
    d = 195075

    #get a distance for each carreau and keep the shortest
    for carreau in carreaux:
        dtempo = carreau[1][0]-(2*carreau[1][1]*r)+rc + carreau[2][0]-(2*carreau[2][1]*g)+gc + carreau[3][0]-(2*carreau[3][1]*b)+bc
        
        if dtempo <= shortest:
            path =  carreau[0]
            break
        elif dtempo <= d:
            #the path of the closest image
            path =  carreau[0]
            d = dtempo

    return path

def calculs_d(rootpath):
    carreauxtemp = os.listdir(rootpath)
    carreaux = []
    for carreau in carreauxtemp:
        imcarreau = PIL.Image.open(os.path.join(rootpath,carreau))
        r2,g2,b2 = resize_image(crop(imcarreau), 1).getdata()[0][:3]
        
        #optimisations/preccalculation
        carreau = [carreau,[r2**2,r2],[g2**2,g2],[b2**2,b2]]
        carreaux += [carreau]

    dlist = []

    for carreau in carreaux:
        for carreau2 in carreaux:
            if carreau2 != carreau:
                dlist.append(carreau2[1][0]-(2*carreau2[1][1]*carreau[1][1])+carreau[1][0] + carreau2[2][0]-(2*carreau2[2][1]*carreau[2][1])+carreau[2][0] + carreau2[3][0]-(2*carreau2[3][1]*carreau[3][1])+carreau[3][0])
    
    
    shortest = min(dlist)

    return (carreaux,shortest)
