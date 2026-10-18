from my_packages.cmd_options_parser  import cmd_options_parser 
from my_packages.generation_types.threshold_generation_type  import threshold_generation_type
from my_packages.generation_types.basic_shapes_generation_type  import basic_shapes_generation_type
from my_packages.generation_types.json_base_generation_type  import json_base_generation_type
from my_packages.refresh  import refresh 
from my_packages.PATHHANDLER import PATHHANDLER

## to do : 
 ## [] complete each generation_type 
 ## [] error handling  { multithreading , path operations , image processing } 
 ## [] add mulithreading either image-based or buffer-stream-based
 ## [] add multiple flags and options handeling to cmd_options_parser 
 ## [] add custom names 
 ## [] add dynamic naming with cmdline options


class Generate : 
    PATHHANDLER.RESOLVE_SOURCE_IMAGES_DIR()

    RUN_MODES = {
            "t_threshold" :  threshold_generation_type , 
            "t_basic-shapes" :  basic_shapes_generation_type , 
            "t_json-base" :  json_base_generation_type , 
            "refresh" : refresh 
                }

    @classmethod
    def generate (cls) :  
        run_modes = cmd_options_parser()
        for run_mode in run_modes : 
            cls.RUN_MODES[run_mode]()


Generate.generate()


