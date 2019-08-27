from __future__ import print_function


def print_t():
    from s import func1
    print(func1())


def func2():
    return {'b': 2}


if __name__ == '__main__':
    print_t()
