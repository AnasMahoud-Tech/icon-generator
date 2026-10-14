import sys
from my_packages.Error_Messages import  Error_Messages

## supports multiple flag and only one option


def validate_options_flag (flag)  : 
    ## flag compability of mixing map 
    flag_chars_map = { 
                      "t"  : { "compatible_combinations" : []  } ,  
                      "r"  : { "compatible_combinations" : []  }   
                  }
    ## [] if not using the arr anymore just make a set directly
    flag_chars_arr =   flag_chars_map.keys()
    flag_chars_set =  set(flag_chars_arr)
    dash_count = flag.count('-')
    chosen_flag_chars = flag[1:]
    chosen_flag_chars_length = len(chosen_flag_chars)
    ## check no flags are passed 
    if chosen_flag_chars_length == 0 : 
        return False 
    temp_filtering_chosen_flag_chars =   list(chosen_flag_chars)

    def exclude_available_flags (char ) : 
        ## using set because set is faster for lookup 
        return char not in     flag_chars_set
    temp_filtering_chosen_flag_chars  = list(filter(exclude_available_flags , temp_filtering_chosen_flag_chars ))

    ## checking flag character compatibility     
    if  chosen_flag_chars_length != 1 :  
    for current_flag_char in list(chosen_flag_chars)  : 
        current_flag_char_compatible_combinations = flag_chars_map[current_flag_char]["compatible_combinations"]
        if   len(current_flag_char_compatible_combinations)  == 0  or chosen_flag_chars not in   current_flag_char_compatible_combinations: 
            return False 

    ## check if the flag has leading dash
    if  dash_count  < 1 or  dash_count  > 1: 
        return False 
    ## check if the flags are only the ones available on the program
    if len(temp_filtering_chosen_flag_chars) != 0   : 
        return False 

    return  True



def validate_option (option  , flag_char_to_option_map  , flags_set , flag_char_to_label_map) : 
    ## [] speed can be improved by changing flag_char_to_label_map  into another scheme with the type of flag as firs key e.g : { "HAS_OPTIONS" : ["t" , "b" , ...]} , "NO_OPTIONS" : [{"r" : "refresh" } , ... ] }
    flag_with_option_support = ""  
    for flag in flag_set  :  
        if flag_char_to_label_map[flag] == "HAS_OPTIONS" : 
           flag_with_option_support  =  flag 
    if option not  in  flag_char_to_option_map[flag_with_option_support] : 
        return False
    return True 



def cmd_options_parser() : 
    flag_char_to_option_map = { 
            "t" : [ 
                   "threshold" , 
                   "json-base" , 
                   "basic-shapes" 
                   ]
            }
    flag_char_to_label_map = {
            "t" : "HAS_OPTIONS" 
            "r" : "refresh"
            }
    ## if no flags given choose default label  
    if (sys.argv) == 1 : 
        return ["t_threshold"]
    
    flag = sys.argv[1] 
    validated_flag = validate_options_flag(flag)
    if validated_flag == False  : 
        ## []  finiish the ERROR message module  
        Error_Messages.display_error_message(cls , Error_Messages.Message_types["CMD_FLAGS_ERROR"] )

    flags_set= set(flag[1:])

    option = sys.argv[2] 
    validated_option = validate_option(option , flag_char_to_option_map , flags_set  , flag_char_to_label_map)
    if validated_option == False  : 
        ## []  finiish the ERROR message module  
        Error_Messages.display_error_message(cls , Error_Messages.Message_types["CMD_OPTIONS_ERROR"] )

    labels  = []
    for flag in flags_set  : 
        flags_label_value =   flag_char_to_label_map[flag]
        if flags_label_value == "HAS_OPTIONS" : 
            ## choose the label matching the option and flag and map it to the flag
            ## it's the option because current implementation only supports one option 
            matching_label = option    
            nested_label =  f"{flag}_{matching_label}}" 
            labels.append(flags_label_value)  
            continue
        labels.append(flags_label_value)  

    return labels 




