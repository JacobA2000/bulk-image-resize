from PIL import Image
from PIL.ExifTags import TAGS

import os
import sys
import getopt

def main(argv):
    global input_dir
    global output_dir

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('python resize.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    
    if len(opts) != 0:
        for opt, arg in opts:
            if opt == '-h':
                print('python resize.py -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                input_dir = arg
            elif opt in ("-o", "--ofile"):
                output_dir = arg
    else:
        print('python resize.py -i <inputfile> -o <outputfile>')
        sys.exit()

    width = input("Width: leave blank to maintain curent width aspect: ")
    height = input("Height: leave blank to maintain curent height aspect: ")

    if width == "":
        width = 0
    else:
        width = int(width)

    if height == "":
        height = 0
    else:
        height = int(height)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            resize(os.path.join(input_dir, filename), width, height)
        else:
            continue

def resize(path, width, height):
    img = Image.open(path)
    exifdata = img.info['exif']

    wsize = width
    hsize = height

    if hsize == 0:
        wpercent = (width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))

    if wsize == 0:
        hpercent = (height / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        
    img = img.resize((wsize, hsize), Image.ANTIALIAS)

    img.save(os.path.join(output_dir, os.path.basename(path)), exif=exifdata, quality=100)

if __name__ == "__main__":
   main(sys.argv[1:])