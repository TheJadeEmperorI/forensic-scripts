"""
Author : The Jade Emperor
Date : 25-06-25

Description :

"""
from datetime import datetime as dt
import os
import sys

def gather_metadata(input_file: str):
    file_info = os.stat(input_file)
    operating_system = sys.platform
    print("OS : ", operating_system)
    
    if "win" in operating_system:
        print("Creation time : ", dt.fromtimestamp(file_info.st_ctime))
        
    elif "linux" in operating_system or "darwin" in operating_system:
        print("Change time : ", dt.fromtimestamp(file_info.st_ctime))
    
    print("Access time : ", dt.fromtimestamp(file_info.st_atime))
    print("Modification time : ", dt.fromtimestamp(file_info.st_mtime))
    
    print("Owner User ID : ", file_info.st_uid)
    print("Group ID : ", file_info.st_gid)
    
    print("File mode : ", file_info.st_mode)
    print("File inode : ", file_info.st_ino)
    
    print("Device ID :", file_info.st_dev)
    
    if "win" not in operating_system:
        major = os.major(stat_info.st_dev)
        minor = os.minor(stat_info.st_dev)
        print("\tMajor : ", major) #type of the device
        print("\tMinor : ", minor) #the partition
    
    print("Number of hard links : ", file_info.st_nlink)
    
    islink = os.path.islink(input_file)
    print("Is a symlink : ", islink)
    if not islink:
        print("File Size : ", file_info.st_size, "bytes") #if it's a symbolic link, it gives the size of the path
    else:
        print("Absolute Path : ", os.path.abspath(input_file))
        print("File Size : ", (os.stat(os.path.abspath(input_file))).st_size, "bytes")
    print("Parent Directory : ", os.path.dirname(input_file))
    
