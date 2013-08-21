""" Captcha.Visual.Tests

Visual CAPTCHA tests

SimpleCaptcha Package
Forked from PyCAPTCHA Copyright (C) 2004 Micah Dowty <micah@navi.cx>
"""
from simplecaptcha.visual import text, backgrounds, distortions, ImageCaptcha
from simplecaptcha import words
import random

__all__ = ["PseudoGimpy", "AngryGimpy", "AntiSpam"]


class PseudoGimpy(ImageCaptcha):
    """A relatively easy CAPTCHA that's somewhat easy on the eyes"""

    def getLayers(self):
        word = words.default_word_list.pick()
        self.addSolution(word)
        return [
            random.choice([
                backgrounds.CroppedImage(),
                backgrounds.TiledImage(),
            ]),
            text.TextLayer(word, borderSize=1),
            distortions.SineWarp(),
            ]


class AngryGimpy(ImageCaptcha):
    """A harder but less visually pleasing CAPTCHA"""

    def getLayers(self):
        word = words.defaultWordList.pick()
        self.addSolution(word)
        return [
            backgrounds.TiledImage(),
            backgrounds.RandomDots(),
            text.TextLayer(word, borderSize=1),
            distortions.WigglyBlocks(),
            ]


class AntiSpam(ImageCaptcha):
    """A fixed-solution CAPTCHA that can be used to hide email addresses or
    URLs from bots"""

    fontFactory = text.FontFactory(20, "vera/VeraBd.ttf")
    defaultSize = (512,50)

    def getLayers(self, solution="murray@example.com"):
        self.addSolution(solution)

        textLayer = text.TextLayer(solution,
                                   borderSize=2,
                                   fontFactory=self.fontFactory)

        return [
            backgrounds.CroppedImage(),
            textLayer,
            distortions.SineWarp(amplitudeRange=(2, 4)),
            ]
