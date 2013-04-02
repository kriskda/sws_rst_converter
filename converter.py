import sys
import os
import re


''' 
    Parent class which contain SAGE_ROOT path. 
    Change before first use.
'''
class Converter(object):
    SAGE_ROOT = "/home/kris/sage/sage-5.6_shit/"

        
class Sws2RstConverter(Converter):

    def __init__(self, sws_file_path):
        self.sws_file_path = sws_file_path

    def __run_sage_converter(self):
        run_expr = self.SAGE_ROOT + "sage" + " -sws2rst " + self.sws_file_path
        os.system(run_expr) 

    def __correct_rst(self):
        rst_file_path = self.sws_file_path.replace(".sws", ".rst")

        try:
            in_file = open(rst_file_path, "r")
            file_line_list = in_file.readlines()      
            in_file.close()
    
            out_file = open(rst_file_path, "w")
            post_subst_list = map(lambda x: re.sub("^::", ".. code-block:: python", x),  file_line_list) 
            post_subst_list = map(lambda x: x.replace("&gt;", ">"),  post_subst_list) 
            post_subst_list = map(lambda x: x.replace("&lt;", "<"),  post_subst_list)
            post_subst_list = map(lambda x: x.replace("&amp;", "&"),  post_subst_list)
            post_subst_list = map(lambda x: x.replace(".. MATH::", "\n.. MATH::"),  post_subst_list)  

            post_subst_list = map(lambda x: re.sub("<[^aA].*?>", "", x),  post_subst_list) 
            post_subst_list = map(lambda x: re.sub("</[^aA].*?>", "", x),  post_subst_list) 

            out_file.write("")
            out_file.write("".join(post_subst_list ))
            out_file.close()
        except IOError as e:
            print "Error: file does not exist !!!"

    def convert(self):
        print "\n1. Sage sws2rst"
        self.__run_sage_converter()

        print "\n2. Correct rst"
        self.__correct_rst()
        print ""


class Rst2SwsConverter(Converter):

    def __init__(self, rst_file_path, sws_file_path):
        self.rst_file_path = rst_file_path
        self.sws_file_path = sws_file_path
   
    def __run_sage_converter(self):
        run_expr = self.SAGE_ROOT + "sage" + " -rst2sws " + self.rst_file_path + " " + self.sws_file_path
        os.system(run_expr) 

    def __correct_rst(self):
        try:
            in_file = open(self.rst_file_path, "r")
            file_line_list = in_file.readlines()      
            in_file.close()
    
            out_file = open(self.rst_file_path, "w")

            post_subst_list = map(lambda x: x.replace(".. code-block:: python", "::"),  file_line_list) 
            post_subst_list = map(lambda x: x.replace(":math:", "").replace(".. MATH::", ""),  post_subst_list) 
            post_subst_list = map(lambda x: re.sub("^...\s*$", "sage: ", x),  post_subst_list) 

            out_file.write("") 
            out_file.write("".join(post_subst_list ))
            out_file.close()
        except IOError as e:
            print "Error: file does not exist !!!"

    def convert(self):
        print "1. Correct rst"
        self.__correct_rst()

        print "\n2. Sage rst2sws"
        self.__run_sage_converter()
        print ""


if __name__ == "__main__":
    param_number = len(sys.argv)

    try:
        if param_number < 3: raise NameError()

        option = sys.argv[1]

        if option == "-sws2rst":
            if param_number != 3: raise NameError()
            
            sws_file_path = sys.argv[2]
            c = Sws2RstConverter(sws_file_path)
        elif option == "-rst2sws":
            if param_number != 4: raise NameError()

            rst_file_path = sys.argv[2]
            sws_file_path = sys.argv[3]
            c = Rst2SwsConverter(rst_file_path, sws_file_path)
        else:
            raise NameError()
        
        c.convert()

    except NameError:
        print "Error: wrong number of parameters!!!\n"
        print "Correct usage:"
        print "python converter.py -sws2rst input.sws"
        print "python converter.py -rst2sws input.rst output.sws"

