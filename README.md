# png_colourizer
This python script can recolourize png images 

## Usage
```
python colourizer.py <image_path> <red> <blue> <green> -> This runs once on the provided arguments
python colourizer.py <input.txt> -> This can run multiple images and colors in one call from the txt input file
```
### Text Input
Text file input is expected to be one image recolourization per line where each line is comma separated. 
``` 
<image_path>, <red>, <blue>, <green> 
<image_path>, <red>, <blue>, <green> 
<image_path>, <red>, <blue>, <green> 
<image_path>, <red>, <blue>, <green> 
<image_path>, <red>, <blue>, <green> 
```
