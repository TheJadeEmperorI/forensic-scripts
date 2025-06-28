"""
Author : The Jade Emperor
Date : 25-06-25

Description :

"""
from datetime import datetime as dt
import os
import sys

def gather_metadata(input_file: str, output_path: str, filters: list, quiet: bool):
    if output_path is not None:
        output_file = open(output_path, "a")
    
    operating_system = sys.platform
    file_info = os.stat(input_file)
    
    if "system" in filters:
        get_system_metadata(file_info,input_file, output_file, operating_system, quiet)
    if "hardware" in filters:
        get_hardware_metadata(file_info, output_file, operating_system, quiet)
    if "user" in filters:
        get_user_metadata(file_info, output_file, quiet)
    if "time" in filters:
        get_time_metadata(file_info, output_file, operating_system, quiet)
        
    if output_path is not None:
        output_file.close()
    
#-- DONT FORGET TO PUT IT OUTPUT_FILE = NONE BY DEFAULT
def get_system_metadata(file_info, input_file: str, output_file: str, operating_system: str, quiet: bool):
    islink = os.path.islink(input_file)
    absolute_path = os.path.abspath(input_file)
    file_size = os.stat(os.path.abspath(input_file)).st_size
    file_mode = file_info.st_mode
    nbr_hard_links = file_info.st_nlink
    parent_directory = os.path.dirname(input_file)
    
    if not quiet:
        print("OS : ", operating_system)
        print("File mode : ", file_mode)
        print("Number of hard links : ", nbr_hard_links)
        print("Is a symlink : ", islink)
        print("Absolute Path : ", absolute_path)
        print("File Size : ", file_size, "bytes")
        print("Parent Directory : ", parent_directory)
    
    if output_file is not None:
        output_file.write("OS : ", operating_system, "\n")
        output_file.write("File mode : ", file_mode, "\n")
        output_file.write("Number of hard links : ", nbr_hard_links, "\n")
        output_file.write("Is a symlink : ", islink, "\n")
        output_file.write("Absolute Path : ", absolute_path, "\n")
        output_file.write("File Size : ", file_size, "\n")
        output_file.write("Parent Directory : ", parent_directory, "\n")
    

def get_hardware_metadata(file_info, output_file: str, operating_system, quiet):
    print("File inode : ", file_info.st_ino)
    print("Device ID :", file_info.st_dev)
    
    if "win" not in operating_system:
        major = os.major(file_info.st_dev)
        minor = os.minor(file_info.st_dev)
        print("\tMajor : ", major) #type of the device
        print("\tMinor : ", minor) #the partition

    
def get_user_metadata(file_info, output_file: str, quiet):
    print("Owner User ID : ", file_info.st_uid)
    print("Group ID : ", file_info.st_gid)
    
    
def get_time_metadata(file_info, output_file: str, operating_system: str, quiet):
    if "win" in operating_system:
        print("Creation time : ", dt.fromtimestamp(file_info.st_ctime))
        
    elif "linux" in operating_system or "darwin" in operating_system:
        print("Change time : ", dt.fromtimestamp(file_info.st_ctime))
    
    print("Access time : ", dt.fromtimestamp(file_info.st_atime))
    print("Modification time : ", dt.fromtimestamp(file_info.st_mtime))
    
