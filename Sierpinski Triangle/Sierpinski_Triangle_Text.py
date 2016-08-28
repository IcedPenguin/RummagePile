#!/bin/python
# -*- coding: iso-8859-15 -*-

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
#
# www.reddit.com/user/IcedPenguin/ wrote this file.  As long as you retain this 
# notice you can do whatever you want with this stuff. If we meet some day, 
# and you think this stuff is worth it, you can buy me a beer in return.   
#
#   -- IcedPenguin
# ----------------------------------------------------------------------------
#

import sys

SYMBOL = "▲"
REVERSE_SYMBOL = "▼"

def generateSierpinksyTriangle(levels, direction):
    triangle = SYMBOL
    size = 1
    while levels > 1:
        triangle, size = buildNextLevel(triangle, size)
        levels -= 1

    if direction == "Down":
        triangle = triangle.replace(SYMBOL, REVERSE_SYMBOL)
        triangle = "\n".join(  triangle.splitlines()[::-1] )

    return triangle
### generateSierpinksyTriangle

def buildNextLevel(triangle, width):
    top_spaces = " " * (width // 2 +1)
    triangle_new = "\n".join([top_spaces + item + top_spaces for item in triangle.splitlines()]) + "\n"
    triangle_new += "\n".join([item + " " + item for item in triangle.splitlines()])
    return triangle_new, (width * 2 +1)
### buildNextLevel

def usage():
    print "usage: python Sierpinski_Triangle_Text.py <levels> <direction [Up/ Down]>"
### usage

def main(args):
    if len(args) != 3:
        usage()
    elif args[2] != "Up" and args[2] != "Down" :
        usage()
    else:    
        try:
            print generateSierpinksyTriangle(int(args[1]), args[2])
        except TypeError:
            usage()
### main

if __name__ == "__main__":
    main(sys.argv)