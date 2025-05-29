### Program that opens a png file and colorizes it to red
from PIL import Image
import sys
import os

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
    if len(sys.argv) != 5:
        print("Usage: python colourizer.py <input_image_path> <red> <green> <blue>")
        sys.exit(1)

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

    
## Run the main function if this script is executed directly
if __name__ == "__main__":
    main()







