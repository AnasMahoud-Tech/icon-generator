from my_packages.generation_steps.removebg import removebg
from my_packages.generation_steps.threshold import threshold
from my_packages.PATHHANDLER import PATHHANDLER




def threshold_generation_type () :
    # list of paths   
    source_images_paths =  PATHHANDLER.SOURCE_IMAGES_PATHS()

    # processing each file 
    for source_image_path in source_images_paths  :  
    
        # removing background and moving it to corresponding directory 
        removed_bg_image_path = removebg(source_image_path ,  PATHHANDLER.RM_BG(source_image_path) )

        # thresholding image and moving it to corresponding directory 
        thresholded_image_path = threshold(removed_bg_image_path ,  PATHHANDLER.THRESHOLDED(removed_bg_image_path) )

        # thresholding image and moving it to corresponding directory 
        PATHHANDLER.move(PATHHANDLER.FINAL_PNG(thresholded_image_path))

        # converting the final png into svg and moving it to corresponding directory        
        convert_png2svg(thresholded_image_path ,  PATHHANDLER.FINAL_SVG(thresholded_image_path) )

    # [] remove after test 
    print("threshold_generation_type")
