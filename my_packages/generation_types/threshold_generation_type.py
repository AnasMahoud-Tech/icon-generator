from my_packages.generation_steps.removebg import removebg
from my_packages.generation_steps.threshold import threshold
from my_packages.generation_steps.convert_png2svg import convert_png2svg
from my_packages.generation_steps.color_range_to_transparent import color_range_to_transparent
from my_packages.PATHHANDLER import PATHHANDLER
from my_packages.refresh import refresh
import sys




def threshold_generation_type () :
    # list of paths   
    
    source_images_paths =  PATHHANDLER.SOURCE_IMAGES_PATHS()
    # processing each file 
    for source_image_path in source_images_paths  :  
    
        # removing background and moving it to corresponding directory 
        removed_bg_image_path = removebg(source_image_path ,  PATHHANDLER.RM_BG(source_image_path) )

        # thresholding image and moving it to corresponding directory 
        thresholded_image_path = threshold(removed_bg_image_path ,  PATHHANDLER.THRESHOLDED(removed_bg_image_path) )

        # turn the white background  transparent 
        color_range_to_change =   "#FFFFFF" 
        target_color_range = "#FFFFFF00" 
        final_result_image = color_range_to_transparent( color_range_to_change , target_color_range , thresholded_image_path , PATHHANDLER.FINAL_RESULT_IMAGE(thresholded_image_path)) 

        # thresholding image and copying it to corresponding directory 
        PATHHANDLER.copy( final_result_image, PATHHANDLER.FINAL_PNG(final_result_image))

        # converting the final png into svg and moving it to corresponding directory        
        convert_png2svg(final_result_image ,  PATHHANDLER.FINAL_SVG(final_result_image) )
        
        # move the processed images into the processed directory 
        PATHHANDLER.move( source_image_path, PATHHANDLER.PROCESSED_IMAGES(source_image_path))
