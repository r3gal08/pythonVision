import cv2
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)


def frame():
    while True:
        _, image = camera.read()
        cv2.imshow('Text Detection', image)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('oppie.jpg', image)
            break
    camera.release()
    cv2.destroyAllWindows()


def tesseract():
    path_to_tesseract = r"/usr/bin/tesseract"
    image_path = "oppie.jpg"  # jpg should be fine especially for live-video as the video is already compressed anyways so
    # images likely can't be degraded any further
    # image_path = "1.png"
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path), config='-l eng --oem 3 --psm 12')
    print(text[:-1])


def testing():
    img = cv2.imread('oppie.jpg', cv2.IMREAD_COLOR)  # Open the image from which charectors has to be recognized
    # img = cv2.resize(img, (620,480) ) #resize the image if required

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grey to reduce detials
    gray = cv2.bilateralFilter(gray, 11, 17, 17)  # Blur to reduce noise

    original = pytesseract.image_to_string(gray, config='')
    #test = (pytesseract.image_to_data(gray, lang=None, config='', nice=0) ) #get confidence level if required
    #print(pytesseract.image_to_boxes(gray))

    print(original)


# tesseract()
testing()
