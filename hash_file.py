"""
Author : The Jade Emperor
Date : 25-06-25

Description :

"""
import hashlib
import psutil
import os
import tqdm

BUFFER_LEVEL = {1: 0.01, 2: 0.10, 3: 0.30, 4: 0.50, 5: 1.00}

ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512
}

def hash_file_content(input_file: str, hash_algorithm: str = "md5",buffer_level: int = 1):
    '''
    Gets the hash of a file's content.
    
    Args :
    input_file : The file's path.
    hash_algorithm : Hash algorithm used.
    buffer_level : The level of RAM used (more informations in the hash-file parser).
    
    Return :
    - The hash of the file's content in hexadecimal.
    '''
    file_content = ALGORITHMS[hash_algorithm]()
    
    #in bytes
    available_ram = psutil.virtual_memory().total
    file_size = os.path.getsize(input_file)
    
    with open(input_file, 'rb') as open_file, tqdm.tqdm(total=file_size, unit="B", unit_scale=True, desc=f"Hashing ({hash_algorithm})") as pbar:
        buff_size = int(available_ram * BUFFER_LEVEL[buffer_level])
        buff = open_file.read(buff_size)

        while buff:
            file_content.update(buff)
            pbar.update(len(buff))
            buff = open_file.read(buff_size)
    
    return file_content.hexdigest()
