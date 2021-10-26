# pip3 install pillow
# pip3 install opencv-python
# pip3 install fitz
# pip3 install PyMuPDF
# pip3 install pytesseract

from PIL import Image
import glob
import os
import pytesseract
import fitz
import re
import pandas as pd


def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    # Open pdf
    pdf = fitz.open(pdfPath)
    # read pdf
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # Setting zoom factor and rotate factor
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # Writing picture
        pm.writePNG(imgPath + str(pg) + ".png")
    pdf.close()


pdf_path = 'Before/ocr/'
img_path = "Before/ocr/"

initial = True
for filename in glob.glob(pdf_path + '/*.pdf'):
    pdf_image(filename, img_path, 5, 5, 0)
    for filename1 in glob.glob(img_path + '/*.png'):
        text = pytesseract.image_to_string(Image.open(filename1), lang='eng')
        year = re.findall(r'(\d{4,4}-\d{2,2})', text)
        Public = re.findall(r'Total public hospitals (\d+ \d+ \d+ \d+ \d+ \d+ \d+ \d+)', text)
        Private = re.findall(r'Total private hospitals (\d+ \d+ \d+ \d+ \d+ \d+ \d+ \d+)', text)
        Beds = re.findall(r'Total beds available in public hospitals (\d*\.?\d* \d*\.?\d* \d*\.?\d* \d*\.?\d* \d*\.?\d* \d*\.?\d* \d*\.?\d* \d*\.?\d*)', text)
        Public = Public[0].split()
        Private = Private[0].split()
        Beds = Beds[0].split()

        state = ['NSW','VIC','QLD','WA','SA','TAS','ACT','NT']

        if initial:
            public = pd.DataFrame({year[0]:Public})
            public.index = [state]

            private = pd.DataFrame({year[0]:Private})
            private.index = [state]

            bed = pd.DataFrame({year[0]:Beds})
            bed.index = [state]
            initial = False

        else:

            public.insert(len(public.columns), year[0], Public, True)
            private.insert(len(private.columns), year[0], Private, True)
            bed.insert(len(bed.columns), year[0], Beds, True)


        #Delete png file
        os.remove(filename1)
# public.to_csv("After/Public_Hospital.csv")
# private.to_csv("After/Private_Hospital.csv")
# bed.to_csv("After/Beds.csv")
print(public)
print(private)
print(bed)


