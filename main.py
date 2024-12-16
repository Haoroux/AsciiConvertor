#Instructions
#1)If you’re converting your webcam video then put video_convert to True
#   Then you have to put an image path into the path variable
#2)you have to select the size you want for your ascii art with the variables wanted_height and wanted_width
#3)optional but you can select wich grayscale you’re using for your art by changing the variable used_gscale by gscale2

#the video convertor will be added in near future 

# importing libs
from cv2 import VideoCapture
import cv2 as cv
import numpy as np


# var

# arrays
gscales = [""" .:-=+*#%@""",
           """ .',;:clodxkO0KXNWM""",
           """ .`:,;'_^"\></-!~=)(|j?}{ ][ti+l7v1%yrfcJ32uIC$zwo96sngaT5qpkYVOL40&mG8*xhedbZUSAQPFDXWK#RNEHBM@"""
           ]



def start_conf():
    convertor_type = int(input("what would you like to convert ? \n 1: your cam \n 2: an image\n"))
    while convertor_type != 1 or convertor_type !=2:
        print("Bro... do you know that you don't look smarter by trying to put something other than the choice offered???? SO")
        convertor_type = int(input("what would you like to convert ? \n 1: your cam \n 2: an image\n"))
        
    wanted_height = int(input("How many lines ?\n")) #wanted mesure/size
    wanted_width = int(input("How many columns ?\n"))
    used_gscale = gscales[int(input("Which gray shade do you want ? \n 1: " + gscales[0] + "\n 2: " + gscales[1] + "\n 3: " + gscales[2] + "\n"))-1]

    if convertor_type == 1:
        cam = VideoCapture(0, cv.CAP_DSHOW)

        while True:
            result, ov_image = cam.read()
            v_image = cv.cvtColor(ov_image, cv.COLOR_BGR2GRAY) 
            if result:
                print(img_ascii_convertor(v_image,wanted_height,wanted_width,used_gscale))
            else:
                print("No image detected. Please try again.")
                break

    elif convertor_type == 2:
        path = input("please paste the path of the image\n").replace("\\", "/").replace('"', '') #path of the image
        # path = "C:/Users/rafae/Documents/prog/python/visual/totoro.webp"
        try:
            image = cv.imread(path)
            gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # rend l’image grise
        except:
            print("It seems that an unexpected error occured, are you sure "+ str(path) + "is the correct path")
            path = input("please paste the path of the image\n").replace("\\", "/").replace('"', '') #path of the image
            
        print(img_ascii_convertor(gray_image,wanted_height,wanted_width,used_gscale))

        save_option = input("would you like to save it ? (y or n)\n")
        if save_option == "y":
            with open("ascii_art.txt", "w") as file:
                print("downloading")
                file.write(img_ascii_convertor(gray_image,wanted_height,wanted_width,used_gscale))
                print("done. See ya!")
        else :
            print("restarting...")
            start_conf()

#convert the image/video in ascii characters
def img_ascii_convertor(image_to_convert,wanted_height,wanted_width, used_gscale):
    divider = 255 / len(used_gscale)
    darkness_array = []
    height, width = image_to_convert.shape

    pixel_height = height // wanted_height
    pixel_width = width // wanted_width


    for h_i in range(wanted_height):
        for w_i in range(wanted_width):
            start_y = h_i * pixel_height
            end_y = (h_i + 1) * pixel_height
            start_x = w_i * pixel_width
            end_x = (w_i + 1) * pixel_width
        
            end_y = min(end_y, height)
            end_x = min(end_x, width)

            block = image_to_convert[start_y:end_y, start_x:end_x]

            # Vérification si le bloc est valide
            if block.size > 0:
                block_mean = np.mean(block)
                # print(f"Block mean: {block_mean}, Block shape: {block.shape}")
            
                if not np.isnan(block_mean):
                    index = int(block_mean // divider)
                    index = min(index, len(used_gscale) - 1)
                    darkness_array.append(used_gscale[index])

    return display_ascii(darkness_array,wanted_height,wanted_width)

#this make the ascii art in the right way
def display_ascii(ascii_array, rows, cols):
    ascii_str = ""
    for i in range(rows):
        ascii_line_array = ascii_array[i*cols: (i+1)*cols]
        ascii_str += ''.join(ascii_line_array) + '\n'
    return ascii_str

start_conf()