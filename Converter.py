import cv2 as cv  #<-- pip install opencv-contrib-python
import Asciify
import Settings

def Image():

    img = cv.imread(Settings.path() + Settings.imgname())         
    cv.imshow('page', img)
    
    Asciify.asciify(img)
    #cv.waitKey(0)


def Video():
          
    vidcap = cv.VideoCapture(Settings.path() + Settings.videoname())
    success, frame = vidcap.read()
    while success:
        #cv.imwrite(Settings.path()+"image_%d.jpg" % count, frame)          #if you want to save every frame of the video
        cv.imshow('page', frame)
        
        Asciify.asciify(frame)  

        success, frame = vidcap.read()
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    vidcap.release()
    cv.destroyAllWindows()


def Webcam():
    capture = cv.VideoCapture(0)            #dipende dalla telecamera, in teoria 0 = default


    while True:   
        success, frame = capture.read()

        cv.imshow('page', frame)
        Asciify.asciify(frame) 

        
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()



def main():

    while True:
        print('Image to Ascii press 1')
        print('Video to Ascii press 2')
        print('Webcam to Ascii press 3')
        res = input()

        if res=='1' or res=='2' or res=='3':
            break
        else:
            print('press 1 xor 2 xor 3')
            

    if res=='1':
        Image()
    elif res=='2':
        Video()
    elif res=='3':
        Webcam()

    



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()