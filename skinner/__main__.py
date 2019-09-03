import sys

from PIL import Image

from . import skin_image

original_image_path = sys.argv[1]
destination_image_path = sys.argv[2]

original_image = Image.open(original_image_path)
skinned_image = skin_image(original_image)
skinned_image.save(destination_image_path)