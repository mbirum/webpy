import sys
from lib.tree import turnTreeOn
from lib.tree import turnTreeOff
from lib.tree import getTree

f = sys.argv[1]
if f == 'on':
     turnTreeOn()
if f == 'off':
     turnTreeOff()
if f == 'get':
     print(getTree())
