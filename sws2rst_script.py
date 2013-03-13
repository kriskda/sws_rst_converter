import sys
import os
import re

SAGE_ROOT = "/home/kris/sage/sage-5.6_shit/"

''' Runs sws2rst of patched sage math '''
def run_sage_converter(sws_file_path):
    run_expr = SAGE_ROOT + "sage" + " -sws2rst " + sws_file_path
    os.system(run_expr) 

''' Does some modification to the rst file i.e. python syntax highlight '''
def correct_sws2rst(rst_file_path):
    in_file = open(rst_file_path, "r")
    file_line_list = in_file.readlines()      
    in_file.close()
    
    out_file = open(rst_file_path, "w")
    post_subst_list = map(lambda x: re.sub("^::", ".. code-block:: python", x),  file_line_list) 

    out_file.write("")
    out_file.write("".join(post_subst_list ))
    out_file.close()

    
if __name__ == "__main__":
    sws_file_path = sys.argv[1]
    rst_file_path = sws_file_path.replace(".sws", ".rst")

    print "1. Sage sws2rst"
    run_sage_converter(sws_file_path)

    print "\n2. Correct rst"
    correct_sws2rst(rst_file_path)
    
    
	
