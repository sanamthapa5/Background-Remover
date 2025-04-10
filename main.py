from rembg import remove
import easygui

from PIL import Image  
inputPath=easygui.fileopenbox(title='select image')
outputPath=easygui.filesavebox(title='Prefered location to save image')

input=Image.open(inputPath)
output=remove(input)
output.save(outputPath)

      