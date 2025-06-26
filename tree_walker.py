"""
Author : The Jade Emperor
Date : 25-06-25

Description :

"""
import os
import hash_file as hf

def scan_directory(path_to_scan: str, hash_algorithm: str=None, output_path: str=None, buffer_level: int=1):
    if output_path is not None:
        output_file = open(output_path, "a")
    
    for root, directories, files in os.walk(path_to_scan):
        for file_entry in files:
            file_path = os.path.join(root, file_entry)
            hash_file = hf.hash_file_content(file_path, hash_algorithm, buffer_level)
            print(file_path)
            
            if output_path is not None:
                output_file.write(file_path + "\t|\t" + hash_file +"\n")
                
                
