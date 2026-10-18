from PIL  import  Image
from  rembg import remove , new_session



def removebg (source_image_path : str , target_path : str )  : 
    # [] handle errors 
    print("in removebg")
    source_image = Image.open(source_image_path).convert("RGB")

    # changing the model to the lighter u2net to avoid triggering OOM  routine which happens on the default install modal BRIA (on less performant machines)
    session = new_session("u2net")
    removed_bg_image = remove(source_image , session=session)
    print("done removebg")

    removed_bg_image.save(target_path , "PNG")

    print("saved removebg")
    return  target_path  
