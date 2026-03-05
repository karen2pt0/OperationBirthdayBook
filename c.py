from PIL import Image, ImageDraw, ImageFont
import os, math

w,h = 1200,1200
img = Image.new("RGB",(w,h),(12,16,22))
draw = ImageDraw.Draw(img)

# subtle gradient
for y in range(h):
    t = y/(h-1)
    r = int(11*(1-t)+20*t)
    g = int(15*(1-t)+26*t)
    b = int(20*(1-t)+30*t)
    draw.line([(0,y),(w,y)], fill=(r,g,b))

# accent ring
cx,cy = w//2,h//2
for i in range(18):
    radius = 360+i
    alpha = max(0, 220 - i*10)
    col = (199,163,106) if i%2==0 else (227,211,180)
    draw.ellipse([cx-radius,cy-radius,cx+radius,cy+radius], outline=col, width=2)

# center circle
draw.ellipse([cx-330,cy-330,cx+330,cy+330], fill=(18,23,31), outline=(60,70,85), width=2)

# text
def load_font(size):
    # Try a few common fonts
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()

title_font = load_font(86)
sub_font = load_font(34)
small_font = load_font(26)

title = "CHRIS"
sub = "Drop your photo here"
small = "Placeholder image • replace with a real photo"

# center text
tw,th = draw.textbbox((0,0), title, font=title_font)[2:]
draw.text((cx-tw/2, cy-90), title, font=title_font, fill=(227,211,180))

sw,sh = draw.textbbox((0,0), sub, font=sub_font)[2:]
draw.text((cx-sw/2, cy+10), sub, font=sub_font, fill=(199,163,106))

mw,mh = draw.textbbox((0,0), small, font=small_font)[2:]
draw.text((cx-mw/2, cy+70), small, font=small_font, fill=(190,190,195))

# small "stamp" bottom
stamp = "In Their Words"
st_font = load_font(28)
stw,sth = draw.textbbox((0,0), stamp, font=st_font)[2:]
draw.rounded_rectangle([cx-stw/2-18, h-140, cx+stw/2+18, h-84], radius=18, outline=(80,90,105), width=2, fill=(16,20,28))
draw.text((cx-stw/2, h-132), stamp, font=st_font, fill=(225,225,225))

out_path = "/mnt/data/chris.jpeg"
img.save(out_path, "JPEG", quality=92)
out_path
