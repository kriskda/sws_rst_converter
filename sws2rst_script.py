import sys
import os

SAGE_ROOT = "/home/kris/sage/sage-5.6_shit/"

def run_sage_converter(sws_file_path):
    run_expr = SAGE_ROOT + "sage" + " -sws2rst " + sws_file_path
    os.system(run_expr) 

def correct_sws2rst(rst_file_path):
    in_file = open(rst_file_path, "r")
    file_line_list = in_file.readlines()      
    in_file.close()
    
    out_file = open(rst_file_path, "w")
    post_subst_list = map(lambda x: x.replace("::", ".. code-block:: python").replace("...   ", "sage: "),  file_line_list) 

    out_file.write("")
    out_file.write("".join(post_subst_list ))
    out_file.close()

    
if __name__ == "__main__":
    sws_file_path = sys.argv[1]
    rst_file_path = sws_file_path.replace(".sws", ".rst")

    run_sage_converter(sws_file_path)
    #correct_sws2rst(rst_file_path)
    
    
	
