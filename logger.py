"""
Author : The Jade Emperor
Date : 25-06-25

Description :

"""
import logging
import sys

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG) #let the user choose the verbosity later

formatter = logging.Formatter("%(asctime)-15s %(funcName)-20s %(levelname)-8s %(message)s")

console_handler = logging.StreamHandler(sys.stdout) 
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

file_handler = logging.FileHandler(r"C:\Users\PC\Desktop\forensic-scripts\emperor_collector\logs\logs.log", mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_tool_usage(mode_selected: str):
    logger.info("The user ran : {}".format(mode_selected))

def log_parser_error():
    logger.error("The user [forgot]/[selected an invalid] option .")
    
def log_file_not_found(filepath):
    logger.error("File not found: {}".format(filepath))