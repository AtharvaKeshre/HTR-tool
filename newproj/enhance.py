
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2

def change(aao):
	path = input(aao).strip()
	image = cv2.imread(path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	cv2.imwrite(filename, gray)
	text = pytesseract.image_to_string(Image.open(filename))
	return text 	