""" Captcha.Visual.Pictures

Random collections of images
"""
#
# PyCAPTCHA Package
# Copyright (C) 2004 Micah Dowty <micah@navi.cx>
#

from Captcha import file
from PIL import Image


class ImageFactory(file.RandomFileFactory):
    """A factory that generates random images from a list"""
    extensions = [".png", ".jpeg"]
    base_path = "pictures"


abstract = ImageFactory("abstract")
nature = ImageFactory("nature")