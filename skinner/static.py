"""
Tuples representing how to crop the resized image
    to fit a minecraft skin

Tuples are in the form
(left, upper, right, lower)
or
(x0, y0, x1, y1)
"""
resized_crops = {
    "head_right": (0, 0, 8, 8),
    "head_front": (8, 0, 16, 8),
    "head_top": (8, 0, 16, 8),
    "head_back": (8, 0, 16, 8),
    "head_bottom": (8, 8, 16, 16),
    "head_left": (16, 0, 24, 8),

    "rightarm_right": (0, 8, 4, 20),
    "rightarm_front": (4, 8, 8, 20),
    "rightarm_top": (4, 4, 8, 8),
    "rightarm_back": (16, 8, 20, 20),
    "rightarm_bottom": (4, 20, 8, 24),
    "rightarm_left": (8, 8, 12, 20),

    "body_right": (4, 8, 8, 20),
    "body_front": (8, 8, 16, 20),
    "body_top": (8, 4, 16, 8),
    "body_back": (8, 8, 16, 20),
    "body_bottom": (8, 20, 16, 24),
    "body_left": (16, 8, 20, 20),

    "leftarm_right": (12, 8, 16, 20),
    "leftarm_front": (16, 8, 20, 20),
    "leftarm_top": (16, 4, 20, 8),
    "leftarm_back": (4, 8, 8, 20),
    "leftarm_bottom": (16, 20, 20, 24),
    "leftarm_left": (20, 8, 24, 20),

    "rightleg_right": (4, 20, 8, 32),
    "rightleg_front": (8, 20, 12, 32),
    "rightleg_top": (8, 16, 12, 20),
    "rightleg_back": (12, 20, 16, 32),
    "rightleg_bottom": (8, 28, 12, 32),
    "rightleg_left": (12, 20, 16, 32),

    "leftleg_right": (8, 20, 12, 32),
    "leftleg_front": (12, 20, 16, 32),
    "leftleg_top": (12, 16, 16, 20),
    "leftleg_back": (8, 20, 12, 32),
    "leftleg_bottom": (12, 28, 16, 32),
    "leftleg_left": (16, 20, 20, 32)
}

"""
Tuples representing how to paste crops
    of an image to createa a usable
    minecraft skin

Tuples are in the form
(left, upper, right, lower)
or
(x0, y0, x1, y1)
"""
skinned_pastes = {
    "head_right": (0, 8, 8, 16),
    "head_front": (8, 8, 16, 16),
    "head_top": (8, 0, 16, 8),
    "head_back": (24, 8, 32, 16),
    "head_bottom": (16, 0, 24, 8),
    "head_left": (16, 8, 24, 16),

    "rightarm_right": (40, 20, 44, 32),
    "rightarm_front": (44, 20, 48, 32),
    "rightarm_top": (44, 16, 48, 20),
    "rightarm_back": (52, 20, 56, 32),
    "rightarm_bottom": (48, 16, 52, 20),
    "rightarm_left": (48, 20, 52, 32),

    "body_right": (16, 20, 20, 32),
    "body_front": (20, 20, 28, 32),
    "body_top": (20, 16, 28, 20),
    "body_back": (32, 20, 40, 32),
    "body_bottom": (28, 16, 36, 20),
    "body_left": (28, 20, 32, 32),

    "leftarm_right": (32, 52, 36, 64),
    "leftarm_front": (36, 52, 40, 64),
    "leftarm_top": (36, 48, 40, 52),
    "leftarm_back": (44, 52, 48, 64),
    "leftarm_bottom": (40, 48, 44, 52),
    "leftarm_left": (40, 52, 44, 64),

    "rightleg_right": (0, 20, 4, 32),
    "rightleg_front": (4, 20, 8, 32),
    "rightleg_top": (4, 16, 8, 20),
    "rightleg_back": (12, 20, 16, 32),
    "rightleg_bottom": (8, 16, 12, 20),
    "rightleg_left": (8, 20, 12, 32),

    "leftleg_right": (16, 52, 20, 64),
    "leftleg_front": (20, 52, 24, 64),
    "leftleg_top": (20, 48, 24, 52),
    "leftleg_back": (28, 52, 32, 64),
    "leftleg_bottom": (24, 48, 28, 52),
    "leftleg_left": (24, 52, 28, 64),
}

"""
These body parts need to be flipped/mirrored
"""
flip = (
    "leftarm_bottom",
    "rightarm_bottom"
)