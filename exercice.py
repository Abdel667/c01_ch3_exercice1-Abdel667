#!/usr/bin/env python
# -*- coding: utf-8 -*-


def square_root(number: int) -> float:
    square_rooted = number**(1/2)
    # TODO completer la fonction
    return square_rooted


def square(number: int) -> int:
    squared= number**2
    # TODO completer la fonction
    return squared


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
