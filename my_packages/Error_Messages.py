import sys



class Error_Messages  : 
	Message_types = { 
                "CMD_FLAGS_ERROR" : "Invalid Flag(s)\nValid uses are as follow:\npython generate.py -t threshold\npython generate.py -t basic-shapes\npython generate.py -t json-base\npython generate.py -r\n" , 
                "CMD_OPTIONS_ERROR" : "Invalid Option\nValid uses are as follow:\npython generate.py -t threshold\npython generate.py -t basic-shapes\npython generate.py -t json-base\n" 
		   }

	@classmethod
	def  display_error_message(cls , Message_type ,  extra_lines="" , order="INSERT" ) :  
        message =  Message_type
        if extra_lines  != "" : 
            if order == "INSERT" :  
                message = extra_lines +   message
            elif order == "APPEND" :  
                message += extra_lines 

		sys.exit(message) 

