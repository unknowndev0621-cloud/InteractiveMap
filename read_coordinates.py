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

