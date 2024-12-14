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


# config var
video_convert = True

path = '' #path of the image

wanted_height = 70 #wanted mesure/size
wanted_width = 140


cam = VideoCapture(0, cv.CAP_DSHOW)
# var




# arrays
gscale = ' .:-=+*#%@'
gscale2 = " .',;:clodxkO0KXNWM"

used_gscale = gscale
divider = 255 / len(used_gscale)


#convert the image/video in ascii characters
def img_ascii_convertor(image_to_convert):
    darkness_array = []
    height, width, channels = image_to_convert.shape

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


if video_convert == False:
    image = cv.imread(path)
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # rend l’image grise
    print(img_ascii_convertor(image))
    with open("ascii_art.txt", "w") as file:
        file.write(img_ascii_convertor(image))


while video_convert == True:
    result, v_image = cam.read()
    
    if result:
        print(img_ascii_convertor(v_image))
    else:
        print("No image detected. Please try again.")
        break