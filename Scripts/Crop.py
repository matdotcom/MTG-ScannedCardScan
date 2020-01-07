from PIL import Image
import json
import sys
import pytesseract
import os
import time
import requests
import re
print( sys.version)
 
         

# Create an Image object from an Image
for f in os.listdir('../Cards'):
    if f.endswith('.png'):
       
        
        imageObject = Image.open('../Cards/'+f).convert('LA')
# Opretter filnavnet og filtypen som variabler. 
        fn, fext = os.path.splitext(f)
        width, height = imageObject.size
        startwidth = width / 12
        startheight = height / 22.3
        width = width - (width / 3.4)
        height = height / 10.9
       
# Crop the name portion of the card
        cropped = imageObject.crop((startwidth,startheight,width,height))
# Display the cropped portion
        cropped.save('../Source/{}_cropped{}'.format(fn,fext))
        im = Image.open('../Source/'+fn+'_cropped'+fext)
# Google tesseract to get a text string from image
        text = pytesseract.image_to_string(im, lang = 'eng')
        time.sleep(0.8)
# Regex expression to help filter out junk from text string
        newtext = re.sub('[^A-Za-z '',]+', '', text)
# GET request to get data about card
        r = requests.get("https://api.scryfall.com/cards/named?fuzzy="+ newtext).json()
        print(newtext)
# Printer prices fæltet i JSON objektet. 
        print(r["prices"])