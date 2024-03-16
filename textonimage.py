from PIL import Image,ImageDraw,ImageFont

def text_on_image(imagepath,text,outputpath):
    image = Image.open(imagepath)

    d=ImageDraw.Draw(image)
    font=ImageFont.truetype("arial.ttf",35)

    TEXT=text
    text_pos = (10,350)
    text_color=(255,0,0)

    d.text(text_pos,text=TEXT,fill=text_color,font=font)

    image.save(f"{outputpath}.png")

