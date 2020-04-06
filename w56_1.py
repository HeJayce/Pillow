from PIL import Image
im = Image.open("E:\OneDrive - mails.cqjtu.edu.cn\AllCode\Python\pic.jpg")
out = im.resize((128, 128))
out = im.rotate(45) # 顺时针角度表示
out.show()