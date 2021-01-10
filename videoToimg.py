import cv2 as cv                                                                #<-- pip install opencv-contrib-python
import Asciify

def Image():
    imgpath='/home/enricolo/Documents/VisualStudioCode/videoterminal/'                  #CAMBIA QUA
    img = cv.imread(imgpath + 'test.jpeg')                                            #CAMBIA QUA
    cv.imshow('page', img)
    
    Asciify.asciify(img)
    #cv.waitKey(0)


def Video():
    videoPath = '/home/enricolo/Documents/VisualStudioCode/videoterminal/'              #CAMBIA QUA
    video=videoPath + 'video.mp4'                                                       #CAMBIA QUA
    vidcap = cv.VideoCapture(video)
    success, frame = vidcap.read()
    count = 1
    while success:
        #if count%12==0:
            #cv.imwrite(videoPath+"files/image_%d.jpg" % count, frame)
        cv.imshow('page', frame)
        
        Asciify.asciify(frame)  

        success, frame = vidcap.read()
        count += 1
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    vidcap.release()
    cv.destroyAllWindows()


def Webcam():
    capture = cv.VideoCapture(0)                                                        #CAMBIA QUA dipende dalla telecamera, in teoria 0 = default
    #capture = cv.VideoCapture(video)

    count = 1
    while True:
        count+=1
        #success, frame = capture.read()
        #cv.imwrite("video_data/image_%d.jpg" % count, image)    
        success, frame = capture.read()

        cv.imshow('page', frame)
        Asciify.asciify(frame) 
        #print('Saved image ', count)
        
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