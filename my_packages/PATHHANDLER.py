import sys 
from pathlib import Path
import os 
import shutil


class  PATHHANDLER : 
    CWD =  str(Path(sys.argv[0]).resolve().parent)
    RESSOURCES_PATH = "" 
    IMAGES_PATH = ""
    
    @classmethod
    def RESOLVE_SOURCE_IMAGES_DIR(cls) :   
        cls.RESSOURCES_PATH =   f"{cls.CWD}{os.path.sep}ressources"
        cls.IMAGES_PATH =   f"{cls.CWD}{os.path.sep}ressources{os.path.sep}Images"
        image_ressources_subdirs = [ "source_images" , "removed_bg_images" , "thresholded_images"  , "result_pngs" , "result_svgs" , "processed_images" ] 
        is_present_dirs_conditions = [
            Path(cls.RESSOURCES_PATH).is_dir() , 
            Path(cls.IMAGES_PATH).is_dir() , 
            Path(f"{cls.IMAGES_PATH}{os.path.sep}source_images").is_dir() , 
            Path(f"{cls.IMAGES_PATH}{os.path.sep}removed_bg_images").is_dir() , 
            Path(f"{cls.IMAGES_PATH}{os.path.sep}thresholded_images").is_dir() , 
            Path(f"{cls.IMAGES_PATH}{os.path.sep}result_pngs").is_dir() , 
            Path(f"{cls.IMAGES_PATH}{os.path.sep}result_svgs").is_dir() ,  
            Path(f"{cls.IMAGES_PATH}{os.path.sep}processed_images").is_dir() 
        ]
        all_ressources_dirs_created = True 
        for is_present_dir in is_present_dirs_conditions :  
            if  is_present_dir == False  :  
                all_ressources_dirs_created = False 
                break 
        if all_ressources_dirs_created == False : 
            for image_ressources_subdir  in image_ressources_subdirs : 
                dirs = Path(cls.CWD) / "ressources"  / "Images" /  image_ressources_subdir
                dirs.mkdir(parents = True , exist_ok = True)
 
 
    @classmethod
    def SOURCE_IMAGES_PATHS(cls ) :   
         # list of source images paths strings
         source_images_paths = [] 
         supported_formats = ["jpg" , "jpeg" , "png"]
         for supported_format in supported_formats  :
             for  soure_image_path in  Path(f"{cls.IMAGES_PATH}{os.path.sep}source_images").glob(f"*.{supported_format}") : 
                 if soure_image_path.is_file() : 
                    source_images_paths.append(str(soure_image_path))
         return source_images_paths
    

    @classmethod 
    def copy(cls , source_path    , target_path) : 
        shutil.copy2(source_path ,target_path )     
     
        
    @classmethod 
    def move(cls , source_path    , target_path) : 
        shutil.move(source_path ,target_path)     

    @classmethod 
    def  move_to_target_dir(cls , abs_path ,   target_dir , ext=True ) :  
        filename_with_ext = abs_path.split(os.path.sep)[-1]
        filename_without_ext =   filename_with_ext.split(".")[0]
        if ext == "dir" : 
            return f"{cls.IMAGES_PATH}{os.path.sep}{target_dir}{os.path.sep}"
        if ext == True :  
            ext = filename_with_ext.split(".")[-1]
        return f"{cls.IMAGES_PATH}{os.path.sep}{target_dir}{os.path.sep}{filename_without_ext}.{ext}"


    @classmethod
    def PROCESSED_IMAGES(cls  , abs_path  ) :   
        return cls.move_to_target_dir( abs_path ,   "processed_images" , "dir" ) 

    @classmethod
    def FINAL_RESULT_IMAGE(cls  , abs_path ) :   
        return cls.move_to_target_dir( abs_path ,   "final_results"  , "png") 

    @classmethod
    def RM_BG(cls , abs_path) :   
        return cls.move_to_target_dir( abs_path ,   "removed_bg_images"  , "png") 

    @classmethod
    def THRESHOLDED(cls , abs_path) :   
        return cls.move_to_target_dir( abs_path ,   "thresholded_images" , "png")  

    @classmethod
    def FINAL_PNG(cls , abs_path) :   
        return cls.move_to_target_dir( abs_path ,   "result_pngs" , "png") 

    @classmethod
    def FINAL_SVG(cls , abs_path) :   
        return cls.move_to_target_dir( abs_path ,   "result_svgs" , "svg") 



