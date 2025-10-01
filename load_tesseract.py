#installed pytesseract
import sys, os, pytesseract

'''
This is a .py for loading tesseract by finding the path containing it in both situation: Local & .exe file 

Be aware you have to add tesseract when you want to bind all files and build .exe file in future
'''
if getattr(sys, 'frozen', False):  
    #When it is running on .exe
    base_path = sys._MEIPASS
    pytesseract.pytesseract.tesseract_cmd = os.path.join(base_path, "tesseract.exe")
    os.environ["TESSDATA_PREFIX"] = os.path.join(base_path, "tessdata")
else:  
    #When it is running on Local for development
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"
