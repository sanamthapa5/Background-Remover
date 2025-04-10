from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Select image')
outputPath = easygui.filesavebox(title='Preferred location to save image', default='*.png')

if inputPath and outputPath:
    try:
        input_image = Image.open(inputPath)
        output = remove(input_image)
        output.save(outputPath)
        print("Image saved successfully.")
    except Exception as e:
        print("Error:", e)
else:
    print("Operation cancelled by user.")
