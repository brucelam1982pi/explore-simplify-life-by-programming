#!/usr/bin/env python3
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#   contact author: brucelam1982pi@gmail.com Bruce

import sys

# english digit
en = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
# french digit
fr = ("zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf")
# chinese digit
cn = ("零", "一", "二", "三", "四", "五", "六", "七", "八", "九")

languageDigit = {'en': en, 'fr': fr, 'cn': cn}
languages = languageDigit.keys()

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} [en|fr] number".format(sys.argv[0]))
        sys.exit()

    args = sys.argv[1:]
    global languages
    language = 'en'
    if args[0].isalpha():
        language = args.pop(0)
    print_digits(args.pop(0), language)


def print_digits(digits, language):
    '''print_digits in language'''
    global languages
    if language not in languages:
        print('Please use 1 language in {0}.'.format(languages))
        return
    dictionary = languageDigit.get(language, en) 

    for digit in digits:
        print(dictionary[int(digit)], end=" ")
    print()

main()
