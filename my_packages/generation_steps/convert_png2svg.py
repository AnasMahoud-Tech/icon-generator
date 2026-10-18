import vtracer 



def convert_png2svg (source_path , target_path ) :   
    print("in vtracer")
   
    vtracer.convert_image_to_svg_py(
            source_path , 
            target_path 
    )

    """
    vtracer.convert_image_to_svg_py(
            source_path , 
            target_path , 
            colormode="bw" , 
            hierarchical="cut"  , 
            corner_threshold=60 , 
            filter_speckle=4
    ) 
    """


    
