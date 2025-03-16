from PIL import Image

def crop_image(image_file):
    # Open the image using Pillow
    image = Image.open(image_file)

    # Get the dimensions of the original image
    width, height = image.size

    # Calculate the size of the square crop
    size = min(width, height)

    # Calculate the coordinates of the crop
    left = (width - size) / 2
    top = (height - size) / 2
    right = (width + size) / 2
    bottom = (height + size) / 2

    # Crop the image
    cropped_image = image.crop((left, top, right, bottom))

    return cropped_image
