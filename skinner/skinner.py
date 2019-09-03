from PIL import Image

from .utils import size_tuple
from .static import resized_crops, skinned_pastes, flip

def skin_image(original_image: Image) -> Image:
    """
    Converts an image to an image that can be
        used as a minecraft skin
    """

    # resize image
    resized_image = original_image.resize(size_tuple({
        "width": 24,
        "height": 32
    }), resample=Image.LANCZOS)

    # crop resized image for every body part
    crops = dict()
    for body_part, bbox in resized_crops.items():
        crops[body_part] = resized_image.crop(box=bbox)
        # flip
        if body_part in flip:
            crops[body_part] = crops[body_part].transpose(Image.FLIP_TOP_BOTTOM)

    # paste every cropped body part
    skinned_image = Image.new(
        mode="RGBA", 
        size=size_tuple({
            "width": 64,
            "height": 64
        }),
        color=(255, 255, 255, 0) # transparent base
    )
    for body_part, bbox in skinned_pastes.items():
        skinned_image.paste(crops[body_part], box=bbox)

    return skinned_image