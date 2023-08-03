from PIL import Image, ImageFont, ImageDraw
import ctypes
import os
filename = 'tasks.txt'

with open(filename) as file:
    tasks = file.readlines()


my_image = Image.open("base.jpg")
title_font = ImageFont.truetype('IndieFlower.ttf', 40)
image_editable = ImageDraw.Draw(my_image)

# Location of the text from top left corner
base_y = 630
base_x = 1000

tasks = [task.replace('\n', "") for task in tasks]

for i in range(len(tasks)):
    image_editable.text((base_x, base_y), str(i+1)+". " + tasks[i],
                        (105, 96, 96), font=title_font)

    base_y += 60

my_image.save("result.jpg")
image_path = os.path.join(os.getcwd(), 'result.jpg')

# Changing the wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 1)
