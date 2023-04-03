import io
import os
import PyPDF2
from PIL import Image, ImageDraw
from pdf2image import convert_from_path

# file path you want to extract images from
file = "D:/Downloads/clientfiles/0324 Petty Cash $40.85-- goes in QUALITY INN DUNDEE (1) - Copy.pdf"

# open the file
with open(file, "rb") as f:
    pdf = PyPDF2.PdfReader(f)
    page = pdf.pages[0]

    # convert the page to an image
    image = convert_from_path(file, first_page=1, last_page=1)[0]

    # display the image
    image.show()

    # select the region
    draw = ImageDraw.Draw(image)
    region =(100, 500, 100, 500) # (left, lower, right, upper)

    # crop the image
    cropped_image = image.crop(region)

    # display the cropped image
    cropped_image.show()


