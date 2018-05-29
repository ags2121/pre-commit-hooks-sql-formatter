import sys
import sqlparse

def main(argv=sys.argv[1:]):
    try:
        #check.main(['--full-report'] + sum((['-r', f] for f in argv), []))
    except SystemExit as error:
        if error.code == 0:
            return 0
        return 1


if __name__ == '__main__':
    sys.exit(main())
