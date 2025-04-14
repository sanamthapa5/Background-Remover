from rembg import remove
import easygui

from PIL import Image  
inputPath=easygui.fileopenbox(title='select image')
outputPath=easygui.filesavebox(title='Your Prefered location to save output image')

input=Image.open(inputPath)
output=remove(input)
output.save(outputPath)

      
