from google.cloud import vision
import io


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    for text in response.text_annotations:
        print(text.description)
        vertices = ['(%s,%s)' % (v.x, v.y) for v in text.bounding_poly.vertices]
        print('bounds:', " ,".join(vertices))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


if __name__ == '__main__':
    print("=" * 30)
    detect_text('./testPhotos/oppie_cropped.jpg')
