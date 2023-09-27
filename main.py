from PIL import Image
from PIL import ImageFilter


class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.changed = []
        self.original = None

    def open(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except IOError:
            print('Файл не найден!')

    def do_gray(self):
        pic_gray = self.original.convert('L')
        pic_gray.save(f'{self.filename[:-4]}_gray.jpg')
        self.changed.append(pic_gray)
        pic_gray.show()

    def blured(self):
        pic_blur = self.original.filter(ImageFilter.GaussianBlur(5))
        pic_blur.save(f'{self.filename[:-4]}_blur.jpg')
        self.changed.append(pic_blur)
        pic_blur.show()

    def flip(self):
        pic_flip = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        pic_flip.save(f'{self.filename[:-4]}_flip.jpg')
        self.changed.append(pic_flip)
        pic_flip.show()

    def up(self):
        pic_up = self.original.transpose(Image.ROTATE_180)
        pic_up.save(f'{self.filename[:-4]}_up.jpg')
        self.changed.append(pic_up)
        pic_up.show()


image = ImageEditor('original.jpg')
image.open()
image.do_gray()
image.blured()
image.flip()
image.up()
