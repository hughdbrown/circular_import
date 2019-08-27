from __future__ import print_function

from s import func1


def print_t():
    print(func1())


def func2():
    return {'b': 2}


if __name__ == '__main__':
    print_t()
