#!/usr/bin/python

#
# Workflow: apply for storage -> supply URL -> analyze content
#

import sys
import getopt

def Usage():
    print '-'*5,'Spider','-'*5
    print 'Web spider usage'
    print '-h, --help: print help message.'
    print '-v, --version: print version.'
    print '-o, --output: input an output file.'
    print '--test: run test.'

def Version():
    print 'Spider 0.0.1'

def main(argv):
    try:
       opts,args = getopt.getopt(argv[1:],'hvo',['help','version','output','test'])
    except getopt.GetoptError, err:
        print str(err)
        Usage()
        sys.exit(2)
    for o,a in opts:
        if o in ('-h','--help'):
            Usage()
            sys.exit(1)
        elif o in ('-v','--version'):
            Version()
            sys.exit(1)
        elif o in ('-o','--output'):
            #ToDo
            sys.exit(1)
        elif o in ('--test'):
            print 'A test'
            sys.exit(1)
        else:
            print 'Unvalid option'
            sys.exit(3)
    

if __name__ == '__main__':
    main(sys.argv)
