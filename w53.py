import os
import glob
from PIL import Image
def shuxing(path):
    a=glob.glob(r'E:\OneDrive - mails.cqjtu.edu.cn\AllCode\Python\pic.jpg')
    for x in a:
        name=os.path.join(path,x)
        im=Image.open(name)
        print(im.format,im.size,im.mode)
if __name__=='__main__':
    path='.'
    shuxing(path)