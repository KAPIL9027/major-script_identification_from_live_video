
from PIL import Image
import pytesseract

import os
import cv2


#name path to image files
image_frames = 'image_frames'

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\Kapil\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

def files():
    try:
        os.remove(image_frames)
    except OSError:
        pass

    if not os.path.exists(image_frames):
        os.makedirs(image_frames)

    # specify the source video path

    src_vid = cv2.VideoCapture('videos\\video.mp4')
    return(src_vid)


def process(src_vid):


    # Use an index to integer.name the files
    index = 0
    while src_vid.isOpened():
        ret, frame = src_vid.read()
        if not ret:
            break

        # name each frame and save as png
        name = './image_frames/frame' + str(index) + '.png'


        # save every 100th frame  (every 4s)
        if index % 100 == 0:
            print('Extracting frames...' + name)
            cv2.imwrite(name,frame)
        index = index + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    src_vid.release()
    cv2.destroyAllWindows()
# do image to text on each png


def get_text():
    for i in os.listdir(image_frames):
        print(str(i))
        my_example = Image.open(image_frames + "/" + i)
        text = pytesseract.image_to_string(my_example,lang='eng')
        print(text)


# main driver
if __name__ == '__main__':
    vid = files()
    process(vid)
    get_text()