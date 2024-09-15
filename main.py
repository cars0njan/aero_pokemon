import pandas as pd
from PIL import Image
import os

# ==== generate a .csv file with count of red pixels in each image =====
def count_red_pixels(image):
    red_pixel_count = 0
    img = image.convert("HSV")
    
    width, height = img.size
    
    for x in range(width):
        for y in range(height):
            h, s, v = img.getpixel((x, y))
            
            if (h >= 0 and h <= 20 and s>= 100 and s <= 255 and  v>= 20 and v <= 255):
                red_pixel_count += 1
            if (h >= 160 and h <= 179 and s>= 100 and s <= 255 and  v>= 20 and v <= 255):
                red_pixel_count += 1
            else:
                pass
                
    return red_pixel_count

def count_images_to_csv():
    df = pd.DataFrame(columns=['filename', 'count'])

    for i in (os.listdir('data/')):
        with Image.open(f'data/{i}') as f:
            count = count_red_pixels(f)
            df.loc[len(df)] = [i, count]
            print(f'{len(df)}/1202 cards')

    df.to_csv('red_count.csv', encoding='utf-8', index=False)
    print('created red_count.csv')

 
count_images_to_csv()

# ==================
