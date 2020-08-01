import RPi.GPIO as GPIO
import web
from lib.tree import turnTreeOn
from lib.tree import turnTreeOff
from lib.tree import getTree

urls = (
    '/', 'index',
    '/tree/on', 'treeon',
    '/tree/off', 'treeoff',
    '/tree', 'gettree'
)

class index:
    def GET(self):
        return "Hello, world!"

class gettree:
     def GET(self):
          return getTree()

class treeon:
     def POST(self):
          turnTreeOn()
          return "Tree on."

class treeoff:
     def POST(self):
          turnTreeOff()
          return "Tree off."

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
