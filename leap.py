import sys


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def main():
    year = int(input('Input the year in question:\n'))
    print(is_leap(year))
    return 0


if __name__ == '__main__':
    sys.exit(main())
