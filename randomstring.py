#!/usr/bin/python3
import string
from random import choice
import argparse

parser = argparse.ArgumentParser(description='Generates random strings')
parser.add_argument('length', metavar='length', type=int, help='The length of generated string')
parser.add_argument('-l', '--lowers', action='store_const', dest='lowers', const=string.ascii_lowercase, default='', help='Adds lower cases to the random string')
parser.add_argument('-u', '--uppers', action='store_const', dest='uppers', const=string.ascii_uppercase, default='', help='Adds upper cases to the random string')
parser.add_argument('-s', '--symbols', action='store_const', dest='symbols', const=string.punctuation, default='', help='Adds symbols to the random string')
parser.add_argument('-w', '--whitespaces', action='store_const', dest='whitespaces', const=string.whitespace, default='', help='Adds whitespaces to the random string')
parser.add_argument('-n', '--numbers', action='store_const', dest='numbers', const=string.digits, default='', help='Adds numbers to the random string')
parser.add_argument('-a', '--all', action='store_const', dest='all', const=string.printable, default='', help='Uses all printable characters in the string generation ( default )')
args = parser.parse_args()
if args.all == '':
  chars = args.lowers + args.uppers + args.symbols + args.whitespaces + args.numbers
  if chars == '':
    chars = string.printable
else:
  chars = args.all

print ("".join(choice(chars) for i in range(args.length)))
