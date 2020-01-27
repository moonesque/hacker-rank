import sys


def one_to_N(n):
    '''a sample docstring'''
    for i in range(1, n+1):
        print(i, end='')
    print('')


def main():
    n = int(input('Input N:\n'))
    one_to_N(n)
    return 0


if __name__ == '__main__':
    sys.exit(main())
