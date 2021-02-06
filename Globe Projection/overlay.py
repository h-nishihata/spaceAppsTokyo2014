import sys
from PIL import Image, ImageDraw

import random

# need to get data from API
# random generated data
data = []
for i in range(20):
    data.append((random.randint(0, 360), random.randint(0, 180)))

im = Image.open(sys.argv[1])
if im.mode != 'RGBA':
  im = im.convert('RGBA')

# pixels per longitude and latitude
pplong = im.size[0] / 360
pplat = im.size[1] / 180

# transparent draw
color_layer = Image.new('RGBA', im.size, color='green')
mask = Image.new('L', im.size, 0)

draw = ImageDraw.Draw(mask)

for point in data:
  longitude = point[0] * pplong
  latitude = point[1] * pplat
  temperature_area = [(longitude - 50, latitude - 50), (longitude + 50, latitude + 50)]
  draw.ellipse(temperature_area, fill=127)

im = Image.composite(color_layer, im, mask)
im.save(sys.argv[2])
