import sys
import sqlparse
import os

def main(argv=sys.argv[1:]):
    try:
        print(argv)
        print(" ".join(argv))
        print("echo '%s' | xargs -I WORD sqlformat WORD -o WORD --wrap_after 90 -k lower" % ' '.join('"{}"'.format(a) for a in argv))
        os.system("echo '%s' | xargs -I WORD sqlformat WORD -o WORD --wrap_after 90 -k lower" % ' '.join('"{}"'.format(a) for a in argv))

        #check.main(['--full-report'] + sum((['-r', f] for f in argv), []))
    except SystemExit as error:
        if error.code == 0:
            return 0
        return 1


if __name__ == '__main__':
    sys.exit(main())
