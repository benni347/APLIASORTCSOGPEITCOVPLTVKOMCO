#!/usr/bin/env python
"""
This is my APLIASORTCSOGPEITCOVPLTVKOMCO interpreter
:Author: benni347@github.com
"""
import sys

valid_string = "A programming language is any set of rules that converts strings, or graphical program elements in the case of visual programming languages, to various kinds of machine code output."


def parse(command):
    if command == valid_string:
        print(valid_string)


code = sys.argv[1]

parse(code)
