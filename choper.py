"""
A module based on pygame to chop image much more easily.
Many extra methods are provided.
"""

from pygame import Surface
from pygame.transform import chop as pgchop

def chop_from(image : Surface, x : int, y : int, w : int, h : int) -> Surface:
    """
    Only return the area you set.
    """

    iw = image.get_width()
    ih = image.get_height()
    image = pgchop(image, [0, 0, x,      y     ]) # UP & LEFT
    image = pgchop(image, [w, h, iw-x-w, ih-y-h]) # DOWN & RIGHT
    return image

def chop_all_from(image : Surface, w : int, h : int) -> list:
    """
    From the `image` chop all pieces of image of a size of `w`,`h`.
    In the order of left -> right,up -> down.
    Stop chopping if pixel is not enough to chop anymore.
    """

    iw = image.get_width()
    ih = image.get_height()
    chopped_list = []

    for y in range(0, ih-h+1, h):
        for x in range(0, iw-w+1, w):
            chopped_list.append(chop_from(image, x, y, w, h))
    return chopped_list
