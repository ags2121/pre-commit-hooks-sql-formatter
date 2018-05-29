import sys
import sqlparse
import os

def main(argv=sys.argv[1:]):
    try:
        print("find %s | xargs -I WORD sqlformat WORD -o WORD --wrap_after 90 --indent_after_first -a -k upper " % ' '.join(argv))
        os.system("find %s | xargs -I WORD sqlformat WORD -o WORD --wrap_after 90 -a -k upper" % ' '.join(argv))

    except SystemExit as error:
        if error.code == 0:
            return 0
        return 1

if __name__ == '__main__':
    sys.exit(main())
