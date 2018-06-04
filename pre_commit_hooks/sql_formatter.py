import sys
import sqlparse
import os

def main(argv=sys.argv[1:]):
    try:
        arg_str = ' '.join(argv)
        os.system("find %s | xargs -I WORD sqlformat WORD -o WORD -k upper -r" % arg_str)
        os.system("""for x in %s; do echo >>"$x"; done""" % arg_str)

    except SystemExit as error:
        if error.code == 0:
            return 0
        return 1

if __name__ == '__main__':
    sys.exit(main())
