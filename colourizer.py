### Program that opens a png file and colorizes it to red
from PIL import Image
import sys
import os

def load_text_file(_input_path):
    try: 
        with open(_input_path, 'r') as file:
            string = file.readlines()
        return string;
    except IOError:
        print(f"Error: Unable to open text file at {_input_path}")
        sys.exit(1)
    
def colour_tuple_to_hex(red, green, blue):
    """
    Convert RGB color tuple to hex string.
    """
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)

def get_image_mask(_image):
    # Create a mask for the image
    mask = Image.new("L", _image.size, 0)
    for x in range(_image.size[0]):
        for y in range(_image.size[1]):
            if _image.getpixel((x, y))[3] > 0:  # Check if pixel is not transparent
                mask.putpixel((x, y), 255)  # Set mask pixel to white
    return mask

def grayscale_image(_image):
    # Convert the image to grayscale
    return _image.convert("L")

def load_image(_input_path):
    # Load the image from the given path
    try:
        img = Image.open(_input_path)

        # conver to RGBA if not already in that mode
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        return img
    except IOError:
        print(f"Error: Unable to open image at {_input_path}")
        sys.exit(1)

    return img


def colorize_image(_input_path, _colour):
    # Open the original image
    origninal_image = load_image(_input_path)

    # Get the image mask
    mask = get_image_mask(origninal_image)

    # get a grayscale version of the image
    grayscale = grayscale_image(origninal_image)

    # Create a new image with the same size as the original
    colorized_image = Image.new("RGBA", origninal_image.size)

    # Fill the new image with the specified color
    for x in range(origninal_image.size[0]):
        for y in range(origninal_image.size[1]):
            if mask.getpixel((x, y)) > 0:  # Check if the pixel is part of the mask
                colorized_image.putpixel((x, y), (_colour[0], _colour[1], _colour[2], grayscale.getpixel((x, y))))
            else:
                colorized_image.putpixel((x, y), (0, 0, 0, 0))  # Transparent pixel

    ## convert the colorized image to RGBA if not already in that mode
    if colorized_image.mode != 'RGBA':
        colorized_image = colorized_image.convert("RGBA")

    ## return the colorized image
    return colorized_image

def main():

    ## If called with 5 arguments, the first is the script name, the next three are RGB values
    if len(sys.argv) == 5:
         ## Parse command line arguments
        input_image_path = sys.argv[1]
        red = int(sys.argv[2])
        green = int(sys.argv[3])
        blue = int(sys.argv[4])
        colour = (red, green, blue)

        ## Get the colorized image
        colorized_image = colorize_image(input_image_path, colour)

        ## Save the colorized image
        colorized_image.save(f"{input_image_path.replace(".png", f"-{colour_tuple_to_hex(red, blue, green)}")}.png");



    ## If called with 2 argument use as text file with comma separated path, R, G, B values. One image recolorized per line.
    if len(sys.argv) == 2:
        input_text_path = sys.argv[1]
        lines = load_text_file(input_text_path)

        for line in lines:
            parts = line.strip().split(',')
            if len(parts) != 4:
                print(f"Error: Invalid line format in {input_text_path}: {line.strip()}")
                continue
            
            input_image_path = parts[0].strip()
            try:
                red = int(parts[1].strip())
                green = int(parts[2].strip())
                blue = int(parts[3].strip())
            except ValueError:
                print(f"Error: Invalid RGB values in {input_text_path}: {line.strip()}")
                continue
            
            colour = (red, green, blue)

            ## Get the colorized image
            colorized_image = colorize_image(input_image_path, colour)

            ## Save the colorized image
            colorized_image.save(f"{input_image_path.replace('.png', f'-{colour_tuple_to_hex(red, blue, green)}')}.png")
        
## Run the main function if this script is executed directly
if __name__ == "__main__":
    main()







