from PIL import Image
im = Image.open("E:\OneDrive - mails.cqjtu.edu.cn\AllCode\Python\pic.jpg")
#out = im.transpose(Image.FLIP_LEFT_RIGHT)
#out = im.transpose(Image.FLIP_TOP_BOTTOM) #颠倒
#out = im.transpose(Image.ROTATE_90)#向左旋转90度
#out = im.transpose(Image.ROTATE_180)#向左旋转180度
out = im.transpose(Image.ROTATE_270)#向左旋转270度
out.show()