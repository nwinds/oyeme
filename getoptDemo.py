"""
getopt/getopt_long demo
=============

C and Python: Basic 
-------------
### example

- -h, getopt
- --help, getopt_long


C vs Python :Diff (simple, incomplete ...)
-------------
### example

#### C
- 'a:'

    $ ./a.out -a12 
    # or
    $ ./a.out -a 12

- 'a::'
    $ ./a.out -a12 #space is a MUST NOT

- extern int declares in getopt.h(i.e, /usr/include/getopt.h)

    - optarg
    - optind
    - opterr - no output to stderr if opterr == 0
    - optopt - getopt returns '?' if lack of required option or invalid option


#### Python
- [VS GNU getopt()](https://docs.python.org/2/library/getopt.html#getopt.getopt "Note")

- TODO


references
-------------

[1]: http://blog.csdn.net/baixue6269/article/details/7550184         "C getopt"
[2]: https://docs.python.org/2/library/getopt.html#module-getopt     "Python module getopt"
[3]: https://docs.python.org/2/library/argparse.html#module-argparse "Further: Python module argparse"

Author: nwinds
"""


import getopt
import sys


def usage():
    print('Usage:')
    print('-h/--help: Help information')
    print('-o/--output: enter an value as an output through stdin')
    # in C there is a much more easy-understanding way to implement
    print('-v: verbose')
    #print(__doc__)
    # TODO: output format


# See https://docs.python.org/2/library/getopt.html for details
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v",            # "short" option args
                                   ["help", "output="])  # C: getopt_long, o required a value behind it
    except getopt.GetoptError as err:  # in C passed in as '?', wrong option entered
        print('O_o\tgetopt.GetoptError: %s' % str(err))
        usage()
        sys.exit(2)  # TODO: return value study

    output = None
    verbose = False
    # in C, use
    # switch(opt):
    # case opt1:
    # case opt2:
    # ...
    # case 'h':// help
    # case '?':// invalid OPTION
    # case ':':// invalid VAR of option opt 
    for o, a in opts:
        if o == '-v':
            verbose = True
        elif o in ('-h', '--help'):  # immutable
            usage()
            sys.exit()
        elif o in ('-o', '--output'):
            output = a
            print('Value entered is %s' % output)
        else:
            assert False, 'Invalid option %s' % o
    if verbose:
        print('Verbose set True')

if __name__ == '__main__':
    main()
