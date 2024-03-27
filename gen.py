# ## Cocktail

# ##### Names


import names
#https://moonbooks.org/Articles/How-to-generate-random-names-first-and-last-names-with-python-/
from quote import quote
from PIL import Image, ImageDraw, ImageFont


cocktail_names = {'GIN FIZZ': 'gin, lemon, sugar, egg, and soda',
                  'LAST WORD': 'gin, green chartreuse, Maraschino liqueur, and lime juice', 
                  'PIÑA COLADA': 'white rum, coconut cream, and pineapple juice',
                 }



def get_quote():
    rand_name = names.get_first_name()
    result = quote(rand_name, limit=10)
    #sentence = result[0]['quote'].split('.')[0] + '.'
    sentences = result[np.random.randint(10)]['quote'].split('.')
    sentence = '"' + '.'.join(result[0]['quote'].split('.')[0:2]) + '..' + '"' 
    author = result[0]['author']
    return (sentence, author)




def text_wrap(text, font, max_width):
        """Wrap text base on specified width. 
        This is to enable text of width more than the image width to be display
        nicely.
        @params:
            text: str
                text to wrap
            font: obj
                font of the text
            max_width: int
                width to split the text with
        @return
            lines: list[str]
                list of sub-strings
        """
        lines = []
        
        # If the text width is smaller than the image width, then no need to split
        # just add it to the line list and return
        if font.getsize(text)[0]  <= max_width:
            lines.append(text)
        else:
            #split the line by spaces to get words
            words = text.split(' ')
            i = 0
            # append every word to a line while its width is shorter than the image width
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                    line = line + words[i]+ " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        return lines


# ##### Picture



from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


def get_a_drink(n):
    
    np.random.seed(seed = n)
    bg = np.random.randint(low=100, high=256, size=(3,)) #(123,209,224) # Background 
    
    oo = (100, 100, 100) # Borders
    lq = np.random.randint(low=100, high=256, size=(3,)) #liquid
    st = lq #straw
    qq = np.clip(np.add(lq, np.random.randint(low=5, high=10, size=(3,))), 0, 255) #clip input to 0-255 #lighter liquid
    bb = np.clip(np.add(qq, np.random.randint(low=10, high=40, size=(3,))), 0, 255) #bubbles
    ff = np.random.randint(low=100, high=256, size=(3,)) #fruit
    fi = np.clip(np.add(ff, np.random.randint(low=10, high=40, size=(3,))), 0, 255) #fruit inside

    pixels_list = [[bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, st, st, st, st, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, st, st, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ff, ff, ff, ff, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, st, st, bg, bg, bg, bg, bg, bg, bg, bg, bg, ff, fi, fi, fi, fi, ff, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, st, st, bg, bg, bg, bg, bg, bg, bg, bg, ff, fi, fi, fi, fi, ff, bg],
               [bg, bg, bg, bg, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, fi, fi, ff, bg],
               [bg, bg, bg, bg, oo, lq, qq, qq, qq, bb, qq, qq, qq, qq, qq, qq, qq, qq, qq, lq, oo, fi, fi, ff, bg],
               [bg, bg, bg, bg, bg, oo, lq, lq, qq, qq, qq, qq, qq, qq, qq, qq, qq, lq, lq, oo, bg, ff, ff, bg, bg],
               [bg, bg, bg, bg, bg, bg, oo, oo, lq, qq, qq, qq, qq, qq, qq, qq, lq, oo, oo, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, oo, lq, qq, qq, bb, qq, qq, lq, oo, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, lq, qq, qq, qq, lq, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, lq, lq, lq, lq, lq, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, oo, oo, oo, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, oo, oo, oo, oo, oo, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, oo, oo, oo, oo, oo, oo, oo, oo, oo, bg, bg, bg, bg, bg, bg, bg, bg],        
               [bg, bg, bg, bg, bg, bg, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, oo, bg, bg, bg, bg, bg, bg],
               [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]]
    
    drink_array = np.array(pixels_list, dtype=np.uint8)
    #drink_image = 
    drink_image = Image.fromarray(drink_array).resize((480, 480), resample=Image.NEAREST)
    #drink_image.save("{}.png".format(n))
    
    
    #text_image
    fontsize = 15
    #get quote
    sentence, author = get_quote()
    #generates blanc canvas
    words_array = np.array(np.zeros((240, 480, 3)), dtype=np.uint8)
    text_image = Image.fromarray(words_array)
    #font
    font_path = 'Press_Start_2P/PressStart2P-Regular.ttf'
    font = ImageFont.truetype(font=font_path, size=fontsize)
    #draw quote
    draw = ImageDraw.Draw(text_image)
    draw.rectangle([(0,0),text_image.size], fill = tuple(bg))
    text_color = 'rgb(100,100,100)'
    x = 20
    y = 40
    line_height = font.getsize('hg')[1] + 5
    lines = text_wrap(sentence, font, text_image.size[0] - x*2) + ['', '       -- {}'.format(author)]
    for line in lines:
        draw.text((x,y), line, fill=text_color, font=font)
        y = y + line_height
        
        
    #text_image.save("{}text.png".format(n))

    
    final_img = get_concat_v(drink_image, text_image)
    final_img.save("{}.png".format(n))




get_a_drink(int(input("Lucky number?\n")))




