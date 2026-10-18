import pyvips
import sys


def threshold(source_path , target_path) : 
    # reading source image  sequentially for better performance  
    source_image  = pyvips.Image.new_from_file(source_path , access="sequential" )

    # remove alpha transparency band if it exists 
    if source_image.bands == 4 :  
        # remove  alpha band from source image
        source_image_without_alpha =   source_image.extract_band( 0 , n=3)
        source_image_alpha =   source_image.extract_band(3)
    
    # making the image black and white 
    source_image_without_alpha.colourspace("b-w")

    thresholded_image =  source_image_without_alpha < 5

    # rejoin the alpha bands
    thresholded_image = thresholded_image.bandjoin(source_image_alpha)

    # source_image.putalpha()

    # choosing bitdepth of 1 for more perfomant png to svg conversion 
    # thresholded_image.write_to_file(target_path , bitdepth=1 )
    thresholded_image.write_to_file(target_path  )

    return target_path 
