"""
Author : The Jade Emperor
Date : 25-06-25

Description :

"""
'''
- répertoire à analyser récursivement
- optionnel : ajouter des filtres avec certains flags sur les metadonnées
- optionnel : ajouter un destination si on veut copier 
- optionnel : choisir une hash function si on veut hash
- optionnel : la verbosité des logs
'''
#-- MODULES --
import argparse
import tree_walker as tw
import gather_metadata as gm
import hash_file as hf
import logger as log
import os
import sys


#-- PROGRAM INFORMATIONS --
__author__ = "The Jade Emperor"
__creation_date__ = "24-06-25"
__description__ = "More informations later"


def main():
    parser = argparse.ArgumentParser(
                 description=__description__,
                 epilog="Author : {} | Creation date : {}".format(__author__, __creation_date__)
                 )
    
    subparsers = parser.add_subparsers(dest="MODE_SELECTED", required=True, help="Selected mode")
    
    #-- TREE-WALKER PARSER --
    parser_tw = subparsers.add_parser("tree-walker", aliases=["tw"], help="later")
    parser_tw.add_argument("SRC", help="Directory path to analyze")
    
    parser_tw.add_argument("--mode",
                           choices=["list-files","hash-files"],
                           default="list-files",
                           help="Later")
    
    parser_tw.add_argument("--hash",
                           choices=["md5", "sha1", "sha256", "sha512"],
                           default="md5",
                           help="Hash all files found with the hash algorithm selected | By default: md5")
    
    
    parser_tw.add_argument("--output-file",
                           "-o",
                           help="Output file's path."
                           )
    
    parser_tw.add_argument("--buffer-level",
                       type=int,
                       choices=[1,2,3,4,5],
                       dest= "buffer_level",
                       default=1, help="The percentage of available RAM to use during the hash :"
                                               "\n\t 1. 1%%"
                                               "\n\t 2. 10%%"
                                               "\n\t 3. 30%%"
                                               "\n\t 4. 50%%"
                                               "\n\t 5. 100%%"
                                               "\n (default 1)"
                       )
    
    #-- GATHER-METADATA --
    parser_gm = subparsers.add_parser("gather-metadata", aliases=["gm"], help="later")
    parser_gm.add_argument("SRC", help="File's path to analyze")
      
    parser_gm.add_argument("--output-file",
                           "-o",
                           help="Output file's path."
                           )
    
    
    #-- HASH-FILE PARSER --
    parser_hf = subparsers.add_parser("hash-file", aliases=["hf"], help="later",formatter_class=argparse.RawTextHelpFormatter)
    parser_hf.add_argument("SRC", help="File path to hash")
    parser_hf.add_argument("--hash",
                           choices=["md5", "sha1", "sha256", "sha512"],
                           help="Hash algorithm to use if needed"
                           )
    
    parser_hf.add_argument("--buffer-level",
                           type=int,
                           choices=[1,2,3,4,5],
                           dest= "buffer_level",
                           default=1, help="The percentage of available RAM to use during the process :"
                                                   "\n\t 1. 1%%"
                                                   "\n\t 2. 10%%"
                                                   "\n\t 3. 30%%"
                                                   "\n\t 4. 50%%"
                                                   "\n\t 5. 100%%"
                                                   "\n (default 1)"
                           )
    
    parser_hf.add_argument("--output-file",
                           "-o",
                           help="Output file's path."
                           )
    
    #-- COPY-FILE PARSER --
    parser_cf = subparsers.add_parser("copy-file", aliases=["cf"], help="later")
    parser_cf.add_argument("SRC", help="File path to hash")
    
    parser_cf.add_argument("--hash",
                           default="md5",
                           help="Hash algorithm to use | By default: md5"
                           )
    
    try:
        args = parser.parse_args()
    except SystemExit as e:
        if e.code == 0:
            sys.exit(0)
        else:
            log.log_parser_error()
            print("One or more fields are incorrect. Use --help (-h) for more informations about the flags.")
            exit(e.code)
    
    log.log_tool_usage(args.MODE_SELECTED)
    
    if args.MODE_SELECTED in {"tree-walker","tw"}:
        try:
            tw.scan_directory(args.SRC,args.hash,args.output_file)
        
        except FileNotFoundError:
            log.log_file_not_found(args.SRC)
            exit(2)
    
    elif args.MODE_SELECTED in {"gather-metadata","gm"}:
        try:
            gm.gather_metadata(args.SRC)
        
        except FileNotFoundError:
            log.log_file_not_found(args.SRC)
            exit(2)
            
        
    elif args.MODE_SELECTED in {"hash-file","hf"}:
        try:
            hf.hash_file_content(args.SRC, args.hash, args.buffer_level)
            
        except FileNotFoundError:
            log.log_file_not_found(args.SRC)
            exit(2)
        
    else:
        pass
    
if __name__ == "__main__":
    main()