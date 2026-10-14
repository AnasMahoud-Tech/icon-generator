import vips 
from my_packages.cmd_options_parser  import cmd_options_parser 
from my_packages.generation_types.threshold_generation_types  import threshold_generation_types 
from my_packages.generation_types.basic_shapes_generation_types  import basic_shapes_generation_types 
from my_packages.generation_types.json_base_generation_types  import json_base_generation_types 
from my_packages.refresh  import refresh 

## to do 
 ## [] complete each generation_type 
 ## [] error handleing 

class Generate : 

    RUN_MODES = {
            "t_threshold" :  threshold_generation_types , 
            "t_basic-shapes" :  basic_shapes_generation_types , 
            "t_json-base" :  json_base_generation_types , 
            "refresh" : refresh 
                }

    @classmethod
    def generate (cls) :  
        run_modes = cmd_options_parser()
        for run_mode in run_modes : 
            RUN_MODES[run_mode]()


Generate.generate()


