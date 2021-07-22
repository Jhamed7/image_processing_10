import cv2
import numpy as np
from PIL import Image
from PIL import ImageFont, ImageDraw, Image


def show_pic(img):
    image = Image.fromarray(img)
    image.show()


background = np.ones((300, 700, 3), dtype=np.uint8)
background[:,:,0] = background[:,:,0] * 87
background[:,:,1] = background[:,:,1] * 83
background[:,:,2] = background[:,:,2] * 82
W = 100

temp = np.copy(background)
colored_square = temp[0:100, 0:100, :]

colored_square[0:47, 0:47, :] = (242, 80, 34)
colored_square[0:47, 53:, :] = (127, 186, 0)
colored_square[53:, 0:47, :] = (0, 164, 239)
colored_square[53:, 53:, :] = (255, 185, 0)

background[100:200, 100:200, :] = colored_square

fontpath = "./Segoe.UI.Bold.ttf"
font = ImageFont.truetype(fontpath, 85)
img_pil = Image.fromarray(background)
draw = ImageDraw.Draw(img_pil)
draw.text((210, 90),  "Microsoft", font = font, fill = (255,255,255,0))
background = np.array(img_pil)

show_pic(background)
