import argparse as ap
import sys
import re

def usage():
    print """
    
    *****************
    SCREENPLAY PARSER
    *****************
    
    Screenplay parser takes a text or html version of a screenplay
    and converts it to a screenplay object for accesible parsing and analysis.
    
    
    Command line Usage:
    
    A) Parse a File
    
        python screenplay_parser.py --file [text/html file]
    
    
    B) Parse Files in a Directory
    
        python screenplay_parser.py --path [directory path to files]

    
    C) Test Module
    
        python screenplay_parser.py --test

    """
    
    return sys.exit(1)


def parse_arguements():

    p = ap.ArgumentParser()
    p.add_argument('--path', help='path directory of screenplay files')
    p.add_argument('--file', help='format of screenplay file')
    p.add_argument('--test', help='test module')
    args = p.parse_args()

    return args


def load_file(file_path):

    print("Loading file from {} ...\n".format(file_path))

    if file_path.endswith('txt'):
        return open(file_path, 'r')
    elif str.endswith('html'):
        return 0
    else:
        print("File Format ending in {} not supported. \n".format(file_path[:-5]))
        pass


def txt_to_json(file):


    for line in file:
        result = re.search(r'((?:EXT\.|INT\.).+)', line)
        if result:
            print result.group()

    return 0

def html_to_json(file):

    return 0



def main():
    args = parse_arguements()
    
    if args.test:
        print "hello"
        sys.exit(1) # run tests
    
    elif args.file:
        # executre parser on file
        file = load_file(args.file)
        txt_to_json(file)
        
    elif args.path:
        print "3"
        sys.exit(1) # execute parser on file in a directory
    
    else:
        usage()
    

    return 0


if __name__ == '__main__':
    main()
