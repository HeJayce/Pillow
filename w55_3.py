from PIL import Image
im = Image.open("E:\OneDrive - mails.cqjtu.edu.cn\AllCode\Python\pic.jpg")
r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))
im.show()