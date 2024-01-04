from PIL import Image, ImageDraw

def drawAndSave(photopath, position, outputpath):
    """
        圖像上座標點畫一個圓圈
    """
    photo = Image.open(photopath)
    draw = ImageDraw.Draw(photo)
    # circle size
    circleSize = 5
    x, y = position[0], position[1]
    draw.ellipse([x-circleSize, y-circleSize, x+circleSize, y+circleSize])
    photo.save(outputpath)

def drawAndSave(photopath, start, end, outputpath):
    """
        圖像上根據起始和結束座標畫一條直線
    """
    photo = Image.open(photopath)
    draw = ImageDraw.Draw(photo)
    draw.line([start, end], fill=(255, 0, 0), width=2)  # 使用紅色顏色和寬度2
    photo.save(outputpath)

# ------------

