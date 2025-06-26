"""
Author : The Jade Emperor
Date : 25-06-25

Description :

"""
import os
import hash_file

def scan_directory(path_to_scan: str, hash_algorithm: str=None, output_path: str=None):
    for root, directories, files in os.walk(path_to_scan):
        for file_entry in files:
            file_path = os.path.join(root, file_entry)
            print(file_path)
