# Bulk Image Resize

A tool built in python utilising the pillow library to bulk resize a folder of images whilst **maintaining exif data**.

## How to use:
1. CD into the directory you cloned this repo to:
    ```sh
    cd clone_location
    ```
1. Install the requirements (Pillow):
    ```sh
    pip install -r requirements.txt
    ```
1. Place all images you wish to bulk resize into a directory and copy the path to that directory.
1. Run the following:
    ```sh
    python resize.py -i "PATH TO THE DIRECTORY OF IMAGES" -o "PATH OF THE DIRECTORY YOU WISH TO SAVE THE RESIZED FILES TO"
    ```