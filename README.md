# Minecraft Skinner

Converts any image to a minecraft-usable skin.

# Usage

* Run from command line

`python -m <original image path> <image destination path>`

* (On Windows) Run with batch file

`skinner.bat`

You will be prompted to enter an original image path and destination image path.

* With python

```
from PIL import Image
from skinner import skin_image

original_image = Image.open("<original image path>")
skinned_image = skin_image(original_image)
skinned_image.save("<image destination path>")
```