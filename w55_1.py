from PIL import Image
im = Image.open("E:\OneDrive - mails.cqjtu.edu.cn\AllCode\Python\pic.jpg")
box = im.copy() #直接复制图像
box = (100, 100, 400, 400)
region = im.crop(box)
region.show()