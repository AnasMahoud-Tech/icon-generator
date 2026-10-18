from PIL  import  Image , ImageColor
import sys


def hex_to_rgba(color_hexcode) :
     
    rgba =  ImageColor.getcolor(color_hexcode , "RGBA")

    return  rgba


def color_range_to_transparent (color_range_to_change , target_color_range_hex , source_image_path , target_image_path ) : 
    source_image = Image.open(source_image_path)
    width , height =    source_image.size
    source_image_pixels = source_image.load()

    # target_color_rgba =  hex_to_rgba(target_color_range_hex)
    target_color_rgba = (255 , 255 , 255 , 255)   

    for x in range(width) : 
        for y in range(height) : 
            if ( source_image_pixels[x , y][3] >  50 )  : 
                source_image_pixels[x , y]  = target_color_rgba

    source_image.save(target_image_path) 
    return target_image_path 

