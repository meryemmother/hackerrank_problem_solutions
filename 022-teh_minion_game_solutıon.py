#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    me = s.split(" ")
    liste = []
    for i in me:
        a = i.capitalize()
        liste.append(a)
        a = (" ".join(liste))
    return a


if __name__ == '__main__':