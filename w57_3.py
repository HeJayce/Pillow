from PIL import ImageEnhance
from PIL import Image
im = Image.open("E:\OneDrive - mails.cqjtu.edu.cn\AllCode\Python\pic.jpg")
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")