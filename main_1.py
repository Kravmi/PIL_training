from PIL import Image
from PIL import ImageFilter

# открой файл с оригиналом картинки
with Image.open('original.jpg') as original:
    original.show()
    print("Размер:", original.size)
    print("Формат:", original.format)
    print('Тип:', original.mode)
# сделай оригинал изображения чёрно-белым
    pic_gray = original.convert('L')
    pic_gray.save('pic_gray.jpg')
    pic_gray.show()
    print("Размер:", pic_gray.size)
    print("Формат:", pic_gray.format)
    print('Тип:', pic_gray.mode)
# сделай оригинал изображения размытым
    pic_blured = original.filter(ImageFilter.GaussianBlur(5))
    pic_blured.save('pic_blured.jpg')
    pic_blured.show()
    print("Размер:", pic_blured.size)
    print("Формат:", pic_blured.format)
    print('Тип:', pic_blured.mode)
# поверни оригинал изображения на 180 градусов
    pic_up = original.transpose(Image.ROTATE_180)
    pic_up.save('pic_up.jpg')
    pic_up.show()
    print("Размер:", pic_up.size)
    print("Формат:", pic_up.format)
    print('Тип:', pic_up.mode)
# зеркальный оригинал изображения
    pic_flip = original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_flip.save('pic_flip.jpg')
    pic_flip.show()
    print("Размер:", pic_flip.size)
    print("Формат:", pic_flip.format)
    print('Тип:', pic_flip.mode)
