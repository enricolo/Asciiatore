import cv2 as cv

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to a new width
def resize_image(image, new_width=230):                                                 #CAMBIA QUA (dimesioni del terminale)
    height, width, depht = image.shape
    ratio = height/width/1.65
    new_height = int(new_width * ratio)
    resized_image = cv.resize(image, (new_width, new_height), interpolation=cv.INTER_AREA)
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    height, width = image.shape

    pixels = list()

    for h in range(height):
        for w in range(width):
            pixels.append(image[h, w])
    
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def asciify(image):

    new_width = 230                                                                     #CAMBIA QUA (dimesioni del terminale)
  
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    printascii (ascii_image)

def printascii(image):
        space = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
        print(space)
        print(image)
        #time.sleep(0.3)
 