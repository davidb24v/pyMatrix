from __future__ import print_function

from PIL import Image

# Default image size
_WIDTH = 16
_HEIGHT = 16


class Frames(object):

    '''
    Turn an image file into a list of 16x16 RGB frames that can
    be sent to an RGB LED display.
    '''

    def __init__(self, fileName, width=_WIDTH, height=_HEIGHT):
        self.width = width
        self.height = height
        img = Image.open(fileName)
        frame = self.__forceSize(img)

        results = [frame]

        # Look for additional frames
        nframes = 0
        while True:
            nframes += 1
            try:
                img.seek(nframes)
            except EOFError:
                break
            results.append(self.__forceSize(img))

        self.images = results
        self.length = len(results)

    def __forceSize(self, img):
        img = img.convert('RGB')
        img.thumbnail((self.width, self.height), Image.ANTIALIAS)
        # check size
        size = img.size
        if size[0] != self.width or size[1] != self.height:
            tmp = Image.new(img.mode, (self.width, self.height))
            tmp.paste(img, (0, 0))
            img = tmp
        return img
