# importing libs
from cv2 import VideoCapture
from pynput.keyboard import *

import cv2 as cv
import numpy as np
import time


# var
i = 0 
path = 'C:/Users/rafae/Documents/prog/python/visual/totoro.webp'
path2 = 'C:/Users/rafae/Documents/prog/python/visual/amous.jpg'

image = cv.imread(path2)
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # rend l’image grise

cam = VideoCapture(0, cv.CAP_DSHOW)


# mesures
wanted_height = 70
wanted_width = 140  


# arrays
gscale = ' .:-=+*#%@'
gscale2 = " .',;:clodxkO0KXNWM"

used_gscale = gscale
divider = 255 / len(used_gscale)


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
            # else:
                # print(f"Block has invalid size: {block.shape}")
    return display_ascii(darkness_array,wanted_height,wanted_width)

def display_ascii(ascii_array, rows, cols):
    ascii_str = ""
    for i in range(rows):
        ascii_line_array = ascii_array[i*cols: (i+1)*cols]
        ascii_str += ''.join(ascii_line_array) + '\n'
    return ascii_str


while True:
    result, v_image = cam.read()
    
    if result:
        print(img_ascii_convertor(v_image))
    else:
        print("No image detected. Please try again.")
        break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# debug
