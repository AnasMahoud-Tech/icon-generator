import sys



class Error_Messages  : 
    Message_types = { 
                     "CMD_FLAGS_ERROR" : " Invalid Flag(s):\n\tValid uses are as follow:\n\tpython generate.py -t threshold\n\tpython generate.py -t basic-shapes\n\tpython generate.py -t json-base\n\tpython generate.py -r" , 
                     "CMD_OPTIONS_ERROR" : " Invalid Option:\n\tValid uses are as follow:\n\tpython generate.py -t threshold\n\tpython generate.py -t basic-shapes\n\tpython generate.py -t json-base"
    }

    @classmethod
    def  display_error_message(cls , message_type ,  extra_lines="" , order="INSERT" ) :  
        message =  message_type
        if extra_lines  != "" : 
            if order == "INSERT" :  
                message = extra_lines +   message
            elif order == "APPEND" :  
                message += extra_lines 

        sys.exit(message) 

