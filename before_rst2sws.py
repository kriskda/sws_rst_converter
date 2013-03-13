import sys, re


def correct_rst2sws(file_path):
    in_file = open(file_path, "r")
    file_line_list = in_file.readlines()      
    in_file.close()
    
    out_file = open(file_path, "w")

    post_subst_list = map(lambda x: x.replace(".. code-block:: python", "::"),  file_line_list) 
    post_subst_list = map(lambda x: x.replace(":math:", "").replace(".. MATH::", ""),  post_subst_list) 
    post_subst_list = map(lambda x: re.sub("^...\s*$", "sage: ", x),  post_subst_list) 

    out_file.write("")
    out_file.write("".join(post_subst_list ))
    out_file.close()

    
if __name__ == "__main__":
    file_path = sys.argv[1]
    correct_rst2sws(file_path)
