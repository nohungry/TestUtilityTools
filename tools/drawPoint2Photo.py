from PIL import Image, ImageDraw

def drawAndSave(photopath, position, outputpath):
    photo = Image.open(photoPath)
    draw = ImageDraw.Draw(photo)
    # circle size
    circleSize = 5
    x, y = position[0], position[1]
    draw.ellipse([x-circleSize, y-circleSize, x+circleSize, y+circleSize)
    photo.save(outputpath)