#Function for returning Coordinates inside of Longvinter
#Required Library: mss, pillow, pytesseract
'''
1) mss:
--> Library for capturing specific area & returning 'ScreenShot' object
--> Gonna use this Object in pillow

2) pillow:
--> Library for creating Image object used in pytesseract
--> it gets the ScreenShot object from mss, and then return Image object

3) pytesseract:
--> Library for changing from img data -> text 
--> Dependency (Pillow)
--> Call Tesseract engine
'''
# capture_ocr.py
import pytesseract
from PIL import Image, ImageOps, ImageFilter
import mss
import load_tesseract
from parse_coordinates import parse_coordinates


def capture_coords(x1: int, y1: int, x2: int, y2: int, lang: str = "eng"):
    """
    Scan a specific area for reading coordinates
    & 
    return x values, y values, and original text just in case
    """
    region = {
        "top": y1,
        "left": x1,
        "width": x2 - x1,
        "height": y2 - y1,
    }

    with mss.mss() as sct:
        screenshot = sct.grab(region)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")

    # For clear, Accurate img
    img = ImageOps.grayscale(img)                 
    img = ImageOps.invert(img)                    
    img = img.point(lambda x: 0 if x < 150 else 255, '1')  
    img = img.filter(ImageFilter.SHARPEN)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)        
    text = pytesseract.image_to_string(img, lang=lang).strip()

    

    y, x = parse_coordinates(text)

    return x, y, text  


