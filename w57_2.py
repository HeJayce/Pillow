from PIL import ImageFilter
from PIL import Image
im = Image.open("E:\OneDrive - mails.cqjtu.edu.cn\AllCode\Python\pic.jpg")
out = im.point(lambda i: i * 1.2)
out.show()